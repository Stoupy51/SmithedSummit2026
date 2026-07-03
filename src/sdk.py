#!/usr/bin/env python3
""" Shader Development Kit for the Smithed Summit 2026.

A small CLI that lets several namespaces ship their own core-shader logic
without fighting over the vanilla files. Each participating namespace drops
GLSL fragments (include/main/header) plus an `sdk.toml` id under
`assets/<ns>/shaders/include/sdk/`, and this tool:

  build  Scan every namespace and generate the combined include/header/inject
         GLSL files under `assets/sdk/shaders/include/build/`. The inject file
         dispatches on a per-surface identifier pixel (see IdentifierPixel)
         through a binary tree of `sdk_id` comparisons.
  patch  Download the vanilla core shaders (from misode's mcmeta mirror) and
         weave the SDK mixin lines into them (see ShaderPatcher), writing the
         result to `assets/minecraft/shaders/core/`.

Run from anywhere inside the project: `python src/sdk.py build|patch`.
"""

import argparse
import tomllib
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import yaml

# Shader pipelines (vanilla core-shader names) and stages the SDK knows how to build.
SUPPORTED_SHADER_PIPELINES: list[str] = ["item"]
SUPPORTED_SHADER_STAGES: list[str] = ["vsh", "fsh"]

# Namespaces never scanned for SDK configs ('minecraft' is vanilla, 'sdk' is the output).
BUILD_IGNORED_NAMESPACES: list[str] = ["minecraft", "sdk"]

# Fallback Minecraft version if it cannot be read from beet.yml.
DEFAULT_MC_VERSION: str = "26.2"


# ── Project configuration (beet.yml) ──────────────────────────────────────────

def find_project_root(start: Path | None = None) -> Path:
    """ Locate the beet project root by walking up from cwd (then this file). """
    bases = [start or Path.cwd(), Path(__file__).resolve().parent]
    for base in bases:
        for directory in [base, *base.parents]:
            if (directory / "beet.yml").is_file() or (directory / "beet.yaml").is_file():
                return directory
    return Path.cwd()


def load_beet_config(project_root: Path) -> dict[str, Any]:
    """ Parse beet.yml (or beet.yaml) at the project root; {} if neither exists. """
    for name in ("beet.yml", "beet.yaml"):
        path = project_root / name
        if path.is_file():
            with open(path, encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
    return {}


def resolve_assets_root(project_root: Path, config: dict[str, Any]) -> Path:
    """ Resolve the resource pack `assets/` folder from the beet configuration. """
    directory = Path(str(config.get("directory", ".")))
    base = directory if directory.is_absolute() else project_root / directory

    resource_pack = cast(dict[str, Any], config.get("resource_pack") or {})
    load = cast("list[str] | str", resource_pack.get("load") or ["."])
    first = load[0] if isinstance(load, list) else load
    return base / first / "assets"


def resolve_mc_version(config: dict[str, Any]) -> str:
    """ The `minecraft` version from the beet config, or DEFAULT_MC_VERSION. """
    return str(config.get("minecraft") or DEFAULT_MC_VERSION)


def load_toml(path: Path) -> dict[str, Any]:
    """ Parse a TOML file, raising FileNotFoundError with a clear message if absent. """
    if not path.is_file():
        raise FileNotFoundError(f"Config file {path} does not exist")
    with open(path, "rb") as f:
        return tomllib.load(f)


# ── Mixin fragments woven into the vanilla shaders ────────────────────────────

# Extra declarations inserted right before the include file (per stage).
INCLUDE_EXTRA_MIXIN_VSH: str = """
uniform sampler2D Sampler0;
""".strip()
INCLUDE_EXTRA_MIXIN_FSH: str = """""".strip()

# Arguments of each namespace's generated main-function wrapper (per stage).
MAIN_ARGS_VSH: str = "ivec2 sdk_iuv, ivec2 sdk_atlasSize"
MAIN_ARGS_FSH: str = ""

# Stage headers: the vsh one reads the identifier pixel pair (marker at the UV,
# id in the pixel right of it) and decodes `sdk_id`; the fsh one bails out early
# on non-SDK surfaces.
HEADER_VSH: str = """
ivec2 sdk_atlasSize = textureSize(Sampler0, 0);
ivec2 sdk_iuv = ivec2(UV0 * sdk_atlasSize);
if (ivec4(texelFetch(Sampler0, sdk_iuv, 0) * 255.0) != ivec4(1, 2, 3, 255)) {sdk_id = 0; return;};
ivec4 sdk_col = ivec4(texelFetch(Sampler0, sdk_iuv + ivec2(1, 0), 0) * 255.0);
sdk_id = (sdk_col.r << 24) | (sdk_col.g << 16) | (sdk_col.b << 8) | sdk_col.a;
""".strip()
HEADER_FSH: str = """
if (sdk_id == 0) return;
""".strip()


def default_main_signature(ns: str, stage: str) -> str:
    """ The GLSL signature of the wrapper generated around a namespace's main.glsl. """
    args = MAIN_ARGS_VSH if stage == "vsh" else MAIN_ARGS_FSH
    return f"void sdk_B_{ns}({args})"


def get_vanilla_source(version: str, pipeline: str, stage: str) -> str:
    """ URL of the vanilla core-shader source on misode's mcmeta mirror. """
    return f"https://raw.githubusercontent.com/misode/mcmeta/refs/tags/{version}-assets/assets/minecraft/shaders/core/{pipeline}.{stage}"


# ── Namespace model ───────────────────────────────────────────────────────────

class IdentifierPixel:
    """ Conversions for the per-namespace identifier pixel.

    Each SDK surface carries a marker pixel followed by an RGBA id pixel; that
    RGBA quadruplet packs into the single signed int the shaders dispatch on. """

    VecType = tuple[int, int, int, int]
    IntType = int

    @staticmethod
    def encode(color: VecType) -> IntType:
        """ Pack an (r, g, b, a) pixel into its signed 32-bit id. """
        return int.from_bytes(color, byteorder="big", signed=True)

    @staticmethod
    def decode(value: IntType) -> VecType:
        """ Unpack a signed 32-bit id back into its (r, g, b, a) pixel. """
        return cast(IdentifierPixel.VecType, value.to_bytes(4, byteorder="big", signed=True))


@dataclass(frozen=True)
class ShaderSource:
    """ One GLSL source file: its content and where it came from. """
    content: str
    path: Path

    @classmethod
    def from_file(cls, path: Path) -> "ShaderSource":
        """ Read a source file, raising FileNotFoundError if it is missing. """
        if not path.is_file():
            raise FileNotFoundError(f"Shader source file {path} does not exist")
        return cls(content=path.read_text("utf-8"), path=path)


@dataclass(frozen=True)
class ShaderStageSources:
    """ The (optional) GLSL fragments a namespace ships for one stage.

    include + main come as a pair (declarations + dispatched body); header is
    an independent fragment inserted right below `#version`. """
    include: ShaderSource | None
    main: ShaderSource | None
    header: ShaderSource | None = None


@dataclass(frozen=True)
class ShaderStage:
    """ One (pipeline, stage) folder of a namespace, e.g. item.vsh/. """
    pipeline: str
    stage: str
    sources: ShaderStageSources
    path: Path


@dataclass(frozen=True)
class ShaderPipeline:
    """ All the stages a namespace ships for one pipeline (e.g. item). """
    name: str
    stages: dict[str, ShaderStage]


class Namespace:
    """ One participating namespace: its sdk.toml config and shader fragments.

    Expects `assets/<name>/shaders/include/sdk/` to contain `sdk.toml` (with the
    namespace's identifier-pixel `id`) and, per (pipeline, stage), an optional
    `<pipeline>.<stage>/` folder holding include.glsl + main.glsl (paired) and/or
    header.glsl. """

    def __init__(self, name: str, assets_root: Path = Path("assets")):
        """ Load the namespace config and discover its shader fragments.

        Raises FileNotFoundError when sdk.toml is missing (the namespace does
        not participate) or when a stage folder has include without main. """
        self.name = name
        self.base_path = assets_root / self.name
        self.sdk_path = self.base_path / "shaders" / "include" / "sdk"
        self.config_path = self.sdk_path / "sdk.toml"
        self.config = load_toml(self.config_path)
        self.pipelines = self.discover_pipelines()

    def id(self) -> IdentifierPixel.VecType:
        """ The namespace's identifier pixel as an (r, g, b, a) quadruplet. """
        return cast(IdentifierPixel.VecType, self.config["id"])

    def id_int(self) -> IdentifierPixel.IntType:
        """ The namespace's identifier pixel packed into its signed 32-bit id. """
        return IdentifierPixel.encode(self.id())

    def stage_path(self, pipeline: str, stage: str) -> Path:
        """ The folder holding this namespace's fragments for (pipeline, stage). """
        return self.sdk_path / f"{pipeline}.{stage}"

    def load_stage(self, pipeline: str, stage: str) -> ShaderStage | None:
        """ Load one (pipeline, stage) folder; None when the namespace ships nothing
        for it. include.glsl and main.glsl must come as a pair (FileNotFoundError
        otherwise); header.glsl is independent. """
        stage_path = self.stage_path(pipeline, stage)
        include_path = stage_path / "include.glsl"
        main_path = stage_path / "main.glsl"
        header_path = stage_path / "header.glsl"

        if not include_path.is_file() and not main_path.is_file() and not header_path.is_file():
            return None

        if include_path.is_file() != main_path.is_file():
            missing = "include.glsl" if not include_path.is_file() else "main.glsl"
            raise FileNotFoundError(f"Shader stage {pipeline}.{stage} in namespace {self.name} is missing {missing}")

        sources = ShaderStageSources(
            include=ShaderSource.from_file(include_path) if include_path.is_file() else None,
            main=ShaderSource.from_file(main_path) if main_path.is_file() else None,
            header=ShaderSource.from_file(header_path) if header_path.is_file() else None,
        )
        return ShaderStage(pipeline=pipeline, stage=stage, sources=sources, path=stage_path)

    def discover_pipelines(self) -> dict[str, ShaderPipeline]:
        """ Load every supported (pipeline, stage) the namespace ships fragments for. """
        pipelines: dict[str, ShaderPipeline] = {}
        for pipeline in SUPPORTED_SHADER_PIPELINES:
            stages = {}
            for stage in SUPPORTED_SHADER_STAGES:
                shader_stage = self.load_stage(pipeline, stage)
                if shader_stage:
                    stages[stage] = shader_stage
            if stages:
                pipelines[pipeline] = ShaderPipeline(name=pipeline, stages=stages)
        return pipelines

    def get_pipeline(self, name: str) -> ShaderPipeline | None:
        """ The namespace's ShaderPipeline named `name`, or None. """
        return self.pipelines.get(name)

    def get_stage(self, pipeline: str, stage: str) -> ShaderStage | None:
        """ The namespace's ShaderStage for (pipeline, stage), or None. """
        shader_pipeline = self.get_pipeline(pipeline)
        return shader_pipeline.stages.get(stage) if shader_pipeline else None


@dataclass
class NamespaceIndex:
    """ Every participating namespace found under the assets root. """
    namespaces: dict[str, Namespace]

    @classmethod
    def from_assets(cls, base_path: Path | None = None) -> "NamespaceIndex":
        """ Scan the assets root for namespaces with a valid sdk.toml, warning
        about (and skipping) the ones without one. """
        root = base_path or Path("assets")
        namespaces: dict[str, Namespace] = {}
        for namespace_dir in root.iterdir():
            if not namespace_dir.is_dir() or namespace_dir.name in BUILD_IGNORED_NAMESPACES:
                continue
            try:
                ns = Namespace(namespace_dir.name, root)
                namespaces[ns.name] = ns
            except FileNotFoundError:
                print(f"Warning: Namespace {namespace_dir.name} does not have a valid sdk.toml config, skipping")
        return cls(namespaces=namespaces)

    def print_registered(self) -> None:
        """ Print every registered namespace with its id and loaded fragments. """
        print("Registered namespaces:")
        for ns in self.namespaces.values():
            print(f" - {ns.name} (id: {ns.id_int()}, vec4{ns.id()})")
            for pipeline in ns.pipelines.values():
                print(f"   - {pipeline.name}")
                for stage in pipeline.stages.values():
                    parts = []
                    if stage.sources.include and stage.sources.main:
                        parts.append("include+main loaded")
                    if stage.sources.header:
                        parts.append("header loaded")
                    print(f"     - {stage.stage} ({', '.join(parts)})")


# ── `build`: generate the combined include/header/inject files ────────────────

@dataclass(frozen=True)
class BuildOptions:
    """ Where the build writes and how the per-namespace wrappers are named. """
    assets_root: Path = Path("assets")
    main_function_signature: Callable[[str, str], str] = default_main_signature

    @property
    def build_root(self) -> Path:
        """ Output folder of the generated GLSL (the `sdk` namespace's build dir). """
        return self.assets_root / "sdk" / "shaders" / "include" / "build"


@dataclass
class ShaderIncludeBuilder:
    """ Generates, per (pipeline, stage), the three combined GLSL files that the
    patched vanilla shaders import:

      header.glsl   every namespace's header fragment (below `#version`)
      include.glsl  every namespace's include fragment + its wrapped main
      inject.glsl   the stage header + a binary tree dispatching `sdk_id` to
                    the matching namespace's wrapper (placed at the end of main)
    """
    index: NamespaceIndex
    options: BuildOptions

    def stage_build_path(self, pipeline: str, stage: str) -> Path:
        """ Output folder for one (pipeline, stage). """
        return self.options.build_root / f"{pipeline}.{stage}"

    def generate_include_content(self, pipeline: str, stage: str) -> str:
        """ The include.glsl body: per namespace, an import of its include.glsl and
        its main.glsl wrapped in the generated main-function signature. """
        chunks = []
        for ns_name, ns in sorted(self.index.namespaces.items()):
            shader_stage = ns.get_stage(pipeline, stage)
            if shader_stage and shader_stage.sources.include and shader_stage.sources.main:
                chunks.append(f"#moj_import <{ns_name}:sdk/{pipeline}.{stage}/include.glsl>")
                signature = self.options.main_function_signature(ns_name, stage)
                main_import = f"#moj_import <{ns_name}:sdk/{pipeline}.{stage}/main.glsl>"
                chunks.append(f"{signature} {{\n{main_import}\n}}")
        return "\n".join(chunks)

    def generate_header_content(self, pipeline: str, stage: str) -> str:
        """ The header.glsl body: one import per namespace header fragment. """
        chunks = []
        for ns_name, ns in sorted(self.index.namespaces.items()):
            shader_stage = ns.get_stage(pipeline, stage)
            if shader_stage and shader_stage.sources.header:
                chunks.append(f"#moj_import <{ns_name}:sdk/{pipeline}.{stage}/header.glsl>")
        return "\n".join(chunks)

    def extract_call(self, signature: str) -> str:
        """ Turn a GLSL function signature into the matching call expression
        (e.g. 'void sdk_B_foo(ivec2 a, ivec2 b)' -> 'sdk_B_foo(a, b)'). """
        head, _, tail = signature.partition("(")
        name = head.strip().split()[-1]
        params = tail.rsplit(")", 1)[0].strip()
        if not params:
            return f"{name}()"
        args = [p.strip().split()[-1] for p in params.split(",") if p.strip()]
        return f"{name}({', '.join(args)})"

    def render_id_tree(self, nodes: list[tuple[int, str]], indent: str = "") -> list[str]:
        """ Render a binary search tree of `sdk_id` comparisons over the sorted
        (id, call) `nodes`, so dispatch cost stays O(log n) namespaces. """
        if not nodes:
            return []
        if len(nodes) == 1:
            return [f"{indent}{nodes[0][1]};"]
        if len(nodes) == 2:
            return [f"{indent}if(sdk_id=={nodes[0][0]}){nodes[0][1]};", f"{indent}else {nodes[1][1]};"]

        mid = len(nodes) // 2
        mid_id, mid_call = nodes[mid]
        left, right = nodes[:mid], nodes[mid + 1:]

        lines = []
        left_lines = self.render_id_tree(left, indent)
        if len(left) == 1:
            lines.append(f"{indent}if(sdk_id<{mid_id}){left_lines[0].strip()}")
        else:
            lines.append(f"{indent}if(sdk_id<{mid_id}){{")
            lines.extend(left_lines)
            lines.append(f"{indent}}}")

        lines.append(f"{indent}else if(sdk_id=={mid_id}){mid_call};")

        if right:
            right_lines = self.render_id_tree(right, indent)
            if len(right) == 1:
                lines.append(f"{indent}else {right_lines[0].strip()}")
            else:
                lines.append(f"{indent}else{{")
                lines.extend(right_lines)
                lines.append(f"{indent}}}")
        return lines

    def build(self) -> None:
        """ Write header.glsl, include.glsl and inject.glsl for every supported
        (pipeline, stage) under the build root. """
        for pipeline in SUPPORTED_SHADER_PIPELINES:
            for stage in SUPPORTED_SHADER_STAGES:
                header = HEADER_VSH if stage == "vsh" else HEADER_FSH
                header += "\n" if header != "" else ""

                build_path = self.stage_build_path(pipeline, stage)
                build_path.mkdir(parents=True, exist_ok=True)

                # Header
                header_content = self.generate_header_content(pipeline, stage)
                (build_path / "header.glsl").write_text(f"#version 330\n{header_content}")

                # Include
                include_content = self.generate_include_content(pipeline, stage)
                (build_path / "include.glsl").write_text(f"#version 330\n{include_content}")

                # Inject
                nodes = []
                for _, ns in sorted(self.index.namespaces.items()):
                    shader_stage = ns.get_stage(pipeline, stage)
                    if shader_stage and shader_stage.sources.include and shader_stage.sources.main:
                        sig = self.options.main_function_signature(ns.name, stage)
                        nodes.append((ns.id_int(), self.extract_call(sig)))

                nodes.sort(key=lambda x: x[0])
                tree_source = "".join(self.render_id_tree(nodes))
                (build_path / "inject.glsl").write_text(f"#version 330\n{header}{tree_source}")


# ── `patch`: weave the SDK imports into a vanilla shader ──────────────────────

class ShaderPatcher:
    """ Weaves the three SDK import lines into a vanilla core-shader source:

      header   right below `#version` (with the vanilla globals re-imported)
      include  the sdk_* varyings + extra mixin + include import, before main
      inject   the dispatch import, as the last line inside main's body

    Patching is idempotent: re-running on an already patched source moves or
    keeps the lines rather than duplicating them. """

    def __init__(self, source: str, pipeline: str, stage: str):
        """ Prepare the patcher for one (pipeline, stage) vanilla `source`. """
        self.lines = source.splitlines()
        self.patched = source
        self.ends_with_newline = source.endswith("\n")
        self.pipeline = pipeline
        self.stage = stage
        self.header_line = f"#moj_import <sdk:build/{pipeline}.{stage}/header.glsl>\n\n#moj_import <minecraft:globals.glsl>"
        self.include_line = f"#moj_import <sdk:build/{pipeline}.{stage}/include.glsl>"
        self.inject_line = f"#moj_import <sdk:build/{pipeline}.{stage}/inject.glsl>"
        # The varyings every SDK namespace can communicate through, declared as
        # outputs in the vertex stage and inputs in the fragment stage.
        qualifier = "out" if stage == "vsh" else "in"
        self.sdk_inputs = [
            f"flat {qualifier} int sdk_id;",
            f"flat {qualifier} int sdk_int;",
            f"flat {qualifier} int sdk_int_b;",
            f"smooth {qualifier} float sdk_float;",
            f"smooth {qualifier} vec4 sdk_vec4;",
            f"smooth {qualifier} vec4 sdk_vec4_b;",
            f"flat {qualifier} ivec4 sdk_ivec4;",
            f"flat {qualifier} mat4 sdk_mat4;",
        ]

    def sync_patched(self) -> None:
        """ Rebuild `patched` from `lines` (preserving the trailing newline). """
        self.patched = "\n".join(self.lines) + ("\n" if self.ends_with_newline else "")

    def insert_after_version(self, line: str) -> None:
        """ Insert (or move) `line` right after the `#version` directive. """
        if line in self.lines:
            self.lines = [existing for existing in self.lines if existing != line]

        version_idx = next((i for i, ln in enumerate(self.lines) if ln.startswith("#version")), -1)
        insert_at = version_idx + 1 if version_idx >= 0 else 0
        self.lines.insert(insert_at, line)
        self.sync_patched()

    def patch_header(self) -> None:
        """ Insert the SDK header import right below `#version`. """
        self.insert_after_version(self.header_line)

    def patch_includes(self) -> None:
        """ Insert the sdk_* varyings, the stage's extra mixin and the include
        import, right before `void main` (or below `#version` when the source
        has no main, keeping the block after an already inserted header). """
        if self.include_line in self.lines:
            self.lines.remove(self.include_line)

        main_idx = next((i for i, ln in enumerate(self.lines) if "void main" in ln), -1)
        if main_idx != -1:
            insert_at = main_idx
        else:
            v_idx = next((i for i, ln in enumerate(self.lines) if ln.startswith("#version")), -1)
            insert_at = v_idx + 1 if v_idx >= 0 else 0

            header_idx = next((i for i, ln in enumerate(self.lines) if ln == self.header_line), -1)
            if header_idx >= insert_at:
                insert_at = header_idx + 1

        if not any(ln.strip() == self.sdk_inputs[0] for ln in self.lines):
            self.lines[insert_at:insert_at] = self.sdk_inputs
            sdk_idx = insert_at
        else:
            sdk_idx = next(i for i, ln in enumerate(self.lines) if ln.strip() == self.sdk_inputs[0])

        include_insert = sdk_idx + len(self.sdk_inputs)

        mixin = INCLUDE_EXTRA_MIXIN_VSH if self.stage == "vsh" else INCLUDE_EXTRA_MIXIN_FSH
        if mixin and not any(ln.strip() == mixin for ln in self.lines):
            self.lines[include_insert:include_insert] = [mixin]
            include_insert += 1

        self.lines.insert(include_insert, self.include_line)
        self.sync_patched()

    def patch_injects(self) -> None:
        """ Insert the inject import as the last statement of main's body,
        matching the file's indentation; a no-op when already present or when
        the source has no main. """
        if self.inject_line in self.patched:
            return

        main_pos = self.patched.find("void main")
        brace_open = self.patched.find("{", main_pos)
        if main_pos == -1 or brace_open == -1:
            return

        # Find main's closing brace by tracking depth from its opening one.
        depth = 0
        insert_at = -1
        for idx in range(brace_open, len(self.patched)):
            if self.patched[idx] == "{":
                depth += 1
            elif self.patched[idx] == "}":
                depth -= 1
                if depth == 0:
                    insert_at = idx
                    break

        if insert_at != -1:
            # Reuse the indentation of main's first body line (fallback: 4 spaces).
            indent = "    "
            for j in range(brace_open + 1, len(self.patched)):
                if self.patched[j] == "\n":
                    next_start = j + 1
                    k = next_start
                    while k < len(self.patched) and self.patched[k] in " \t":
                        k += 1
                    if k > next_start:
                        indent = self.patched[next_start:k]
                    break

            self.patched = self.patched[:insert_at] + f"{indent}{self.inject_line}\n" + self.patched[insert_at:]

    def apply(self) -> str:
        """ Run all three patches and return the patched source. """
        self.patch_header()
        self.patch_includes()
        self.patch_injects()
        return self.patched


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_command(args: argparse.Namespace) -> None:
    """ `sdk build`: scan the namespaces and generate the combined GLSL files. """
    project_root = find_project_root()
    config = load_beet_config(project_root)
    assets_root = resolve_assets_root(project_root, config)

    print(f"Using assets root: {assets_root}")
    index = NamespaceIndex.from_assets(assets_root)
    index.print_registered()
    ShaderIncludeBuilder(index=index, options=BuildOptions(assets_root=assets_root)).build()


def patch_command(args: argparse.Namespace) -> None:
    """ `sdk patch`: download the vanilla shaders and weave the SDK mixins in. """
    project_root = find_project_root()
    config = load_beet_config(project_root)
    assets_root = resolve_assets_root(project_root, config)
    version = args.version or resolve_mc_version(config)

    core_path = assets_root / "minecraft" / "shaders" / "core"
    core_path.mkdir(parents=True, exist_ok=True)
    print(f"Patching vanilla {version} sources into: {core_path}")

    for pipeline in SUPPORTED_SHADER_PIPELINES:
        for stage in SUPPORTED_SHADER_STAGES:
            url = get_vanilla_source(version, pipeline, stage)
            with urllib.request.urlopen(url) as response:
                content = response.read().decode("utf-8")

            patched_content = ShaderPatcher(content, pipeline, stage).apply()
            (core_path / f"{pipeline}.{stage}").write_text(patched_content)


def main() -> None:
    """ Parse the CLI arguments and dispatch to the matching command. """
    parser = argparse.ArgumentParser(prog="sdk")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Build the shader index")
    build_parser.set_defaults(func=build_command)

    patch_parser = subparsers.add_parser("patch", help="Download and apply injection mixins to vanilla sources")
    patch_parser.add_argument(
        "--version", "-v", default=None, help="Minecraft version to download (defaults to beet.yml's `minecraft`)"
    )
    patch_parser.set_defaults(func=patch_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

