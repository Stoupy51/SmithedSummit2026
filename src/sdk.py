#!/usr/bin/env python3
"""
Shader Development Kit for the Smithed Summit 2026.
"""

import argparse
import tomllib
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import yaml

_SUPPORTED_SHADER_PIPELINES = ["item"]
_SUPPORTED_SHADER_STAGES = ["vsh", "fsh"]
_BUILD_IGNORED_NAMESPACES = ["minecraft", "sdk"]

# Fallback Minecraft version if it cannot be read from beet.yml.
_DEFAULT_MC_VERSION = "26.2"


def find_project_root(start: Path | None = None) -> Path:
    """Locate the beet project root by walking up from cwd (then this file)."""
    bases = [start or Path.cwd(), Path(__file__).resolve().parent]
    for base in bases:
        for directory in [base, *base.parents]:
            if (directory / "beet.yml").is_file() or (directory / "beet.yaml").is_file():
                return directory
    return Path.cwd()


def load_beet_config(project_root: Path) -> dict[str, Any]:
    for name in ("beet.yml", "beet.yaml"):
        path = project_root / name
        if path.is_file():
            with open(path, encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
    return {}


def resolve_assets_root(project_root: Path, config: dict[str, Any]) -> Path:
    """Resolve the resource pack `assets/` folder from the beet configuration."""
    directory = Path(str(config.get("directory", ".")))
    base = directory if directory.is_absolute() else project_root / directory

    resource_pack = cast(dict[str, Any], config.get("resource_pack") or {})
    load = cast("list[str] | str", resource_pack.get("load") or ["."])
    first = load[0] if isinstance(load, list) else load
    return base / first / "assets"


def resolve_mc_version(config: dict[str, Any]) -> str:
    return str(config.get("minecraft") or _DEFAULT_MC_VERSION)

_INCLUDE_EXTRA_MIXIN_VSH = """
uniform sampler2D Sampler0;
""".strip()
_MAIN_ARGS_VSH = "ivec2 sdk_iuv, ivec2 sdk_atlasSize"
_HEADER_VSH = """
ivec2 sdk_atlasSize = textureSize(Sampler0, 0);
ivec2 sdk_iuv = ivec2(UV0 * sdk_atlasSize);
if (ivec4(texelFetch(Sampler0, sdk_iuv, 0) * 255.0) != ivec4(1, 2, 3, 255)) {sdk_id = 0; return;};
ivec4 sdk_col = ivec4(texelFetch(Sampler0, sdk_iuv + ivec2(1, 0), 0) * 255.0);
sdk_id = (sdk_col.r << 24) | (sdk_col.g << 16) | (sdk_col.b << 8) | sdk_col.a;
""".strip()

_INCLUDE_EXTRA_MIXIN_FSH = """""".strip()
_MAIN_ARGS_FSH = ""
_HEADER_FSH = """
if (sdk_id == 0) return;
""".strip()


def default_main_signature(ns: str, stage: str) -> str:
    args = _MAIN_ARGS_VSH if stage == "vsh" else _MAIN_ARGS_FSH

    return f"void sdk_B_{ns}({args})"


def get_vanilla_source(version: str, pipeline: str, stage: str) -> str:
    return f"https://raw.githubusercontent.com/misode/mcmeta/refs/tags/{version}-assets/assets/minecraft/shaders/core/{pipeline}.{stage}"


def load_toml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Config file {path} does not exist")
    with open(path, "rb") as f:
        return tomllib.load(f)


class IdentifierPixel:
    VecType = tuple[int, int, int, int]
    IntType = int

    @staticmethod
    def encode(color: VecType) -> IntType:
        return int.from_bytes(color, byteorder="big", signed=True)

    @staticmethod
    def decode(value: IntType) -> VecType:
        return cast(IdentifierPixel.VecType, value.to_bytes(4, byteorder="big", signed=True))


@dataclass(frozen=True)
class ShaderSource:
    content: str
    path: Path

    @classmethod
    def from_file(cls, path: Path) -> "ShaderSource":
        if not path.is_file():
            raise FileNotFoundError(f"Shader source file {path} does not exist")
        return cls(content=path.read_text("utf-8"), path=path)


@dataclass(frozen=True)
class ShaderStageSources:
    include: ShaderSource | None
    main: ShaderSource | None
    header: ShaderSource | None = None


@dataclass(frozen=True)
class ShaderStage:
    pipeline: str
    stage: str
    sources: ShaderStageSources
    path: Path


@dataclass(frozen=True)
class ShaderPipeline:
    name: str
    stages: dict[str, ShaderStage]


class Namespace:
    def __init__(self, name: str, assets_root: Path = Path("assets")):
        self.name = name
        self.base_path = assets_root / self.name
        self.sdk_path = self.base_path / "shaders" / "include" / "sdk"
        self.config_path = self.sdk_path / "sdk.toml"
        self.config = load_toml(self.config_path)
        self.pipelines = self._discover_pipelines()

    def id(self) -> IdentifierPixel.VecType:
        return cast(IdentifierPixel.VecType, self.config["id"])

    def id_int(self) -> IdentifierPixel.IntType:
        return IdentifierPixel.encode(self.id())

    def _get_stage_path(self, pipeline: str, stage: str) -> Path:
        return self.sdk_path / f"{pipeline}.{stage}"

    def _load_stage(self, pipeline: str, stage: str) -> ShaderStage | None:
        stage_path = self._get_stage_path(pipeline, stage)
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

    def _discover_pipelines(self) -> dict[str, ShaderPipeline]:
        pipelines: dict[str, ShaderPipeline] = {}
        for pipeline in _SUPPORTED_SHADER_PIPELINES:
            stages = {}
            for stage in _SUPPORTED_SHADER_STAGES:
                shader_stage = self._load_stage(pipeline, stage)
                if shader_stage:
                    stages[stage] = shader_stage
            if stages:
                pipelines[pipeline] = ShaderPipeline(name=pipeline, stages=stages)
        return pipelines

    def get_pipeline(self, name: str) -> ShaderPipeline | None:
        return self.pipelines.get(name)

    def get_stage(self, pipeline: str, stage: str) -> ShaderStage | None:
        shader_pipeline = self.get_pipeline(pipeline)
        return shader_pipeline.stages.get(stage) if shader_pipeline else None


@dataclass
class NamespaceIndex:
    namespaces: dict[str, Namespace]

    @classmethod
    def from_assets(cls, base_path: Path | None = None) -> "NamespaceIndex":
        root = base_path or Path("assets")
        namespaces: dict[str, Namespace] = {}
        for namespace_dir in root.iterdir():
            if not namespace_dir.is_dir() or namespace_dir.name in _BUILD_IGNORED_NAMESPACES:
                continue
            try:
                ns = Namespace(namespace_dir.name, root)
                namespaces[ns.name] = ns
            except FileNotFoundError:
                print(f"Warning: Namespace {namespace_dir.name} does not have a valid sdk.toml config, skipping")
        return cls(namespaces=namespaces)

    def print_registered(self) -> None:
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


@dataclass(frozen=True)
class BuildOptions:
    assets_root: Path = Path("assets")
    main_function_signature: Callable[[str, str], str] = default_main_signature

    @property
    def build_root(self) -> Path:
        return self.assets_root / "sdk" / "shaders" / "include" / "build"


@dataclass
class ShaderIncludeBuilder:
    index: NamespaceIndex
    options: BuildOptions

    def _stage_build_path(self, pipeline: str, stage: str) -> Path:
        return self.options.build_root / f"{pipeline}.{stage}"

    def _generate_include_content(self, pipeline: str, stage: str) -> str:
        chunks = []
        for ns_name, ns in sorted(self.index.namespaces.items()):
            shader_stage = ns.get_stage(pipeline, stage)
            if shader_stage and shader_stage.sources.include and shader_stage.sources.main:
                chunks.append(f"#moj_import <{ns_name}:sdk/{pipeline}.{stage}/include.glsl>")
                signature = self.options.main_function_signature(ns_name, stage)
                main_import = f"#moj_import <{ns_name}:sdk/{pipeline}.{stage}/main.glsl>"
                chunks.append(f"{signature} {{\n{main_import}\n}}")
        return "\n".join(chunks)

    def _generate_header_content(self, pipeline: str, stage: str) -> str:
        chunks = []
        for ns_name, ns in sorted(self.index.namespaces.items()):
            shader_stage = ns.get_stage(pipeline, stage)
            if shader_stage and shader_stage.sources.header:
                chunks.append(f"#moj_import <{ns_name}:sdk/{pipeline}.{stage}/header.glsl>")
        return "\n".join(chunks)

    def _extract_call(self, signature: str) -> str:
        head, _, tail = signature.partition("(")
        name = head.strip().split()[-1]
        params = tail.rsplit(")", 1)[0].strip()
        if not params:
            return f"{name}()"
        args = [p.strip().split()[-1] for p in params.split(",") if p.strip()]
        return f"{name}({', '.join(args)})"

    def _render_id_tree(self, nodes: list[tuple[int, str]], indent: str = "") -> list[str]:
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
        left_lines = self._render_id_tree(left, indent)
        if len(left) == 1:
            lines.append(f"{indent}if(sdk_id<{mid_id}){left_lines[0].strip()}")
        else:
            lines.append(f"{indent}if(sdk_id<{mid_id}){{")
            lines.extend(left_lines)
            lines.append(f"{indent}}}")

        lines.append(f"{indent}else if(sdk_id=={mid_id}){mid_call};")

        if right:
            right_lines = self._render_id_tree(right, indent)
            if len(right) == 1:
                lines.append(f"{indent}else {right_lines[0].strip()}")
            else:
                lines.append(f"{indent}else{{")
                lines.extend(right_lines)
                lines.append(f"{indent}}}")
        return lines

    def build(self) -> None:
        for pipeline in _SUPPORTED_SHADER_PIPELINES:
            for stage in _SUPPORTED_SHADER_STAGES:
                header = _HEADER_VSH if stage == "vsh" else _HEADER_FSH
                header += "\n" if header != "" else ""

                build_path = self._stage_build_path(pipeline, stage)
                build_path.mkdir(parents=True, exist_ok=True)

                # Header
                header_content = self._generate_header_content(pipeline, stage)
                (build_path / "header.glsl").write_text(f"#version 330\n{header_content}")

                # Include
                include_content = self._generate_include_content(pipeline, stage)
                (build_path / "include.glsl").write_text(f"#version 330\n{include_content}")

                # Inject
                nodes = []
                for _, ns in sorted(self.index.namespaces.items()):
                    shader_stage = ns.get_stage(pipeline, stage)
                    if shader_stage and shader_stage.sources.include and shader_stage.sources.main:
                        sig = self.options.main_function_signature(ns.name, stage)
                        nodes.append((ns.id_int(), self._extract_call(sig)))

                nodes.sort(key=lambda x: x[0])
                tree_source = "".join(self._render_id_tree(nodes))
                (build_path / "inject.glsl").write_text(f"#version 330\n{header}{tree_source}")


class ShaderPatcher:
    def __init__(self, source: str, pipeline: str, stage: str):
        self.lines = source.splitlines()
        self.patched = source
        self.ends_with_newline = source.endswith("\n")
        self.pipeline = pipeline
        self.stage = stage
        self.header_line = f"#moj_import <sdk:build/{pipeline}.{stage}/header.glsl>\n\n#moj_import <minecraft:globals.glsl>"
        self.include_line = f"#moj_import <sdk:build/{pipeline}.{stage}/include.glsl>"
        self.inject_line = f"#moj_import <sdk:build/{pipeline}.{stage}/inject.glsl>"
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

    def _sync_patched(self) -> None:
        self.patched = "\n".join(self.lines) + ("\n" if self.ends_with_newline else "")

    def _insert_after_version(self, line: str) -> None:
        if line in self.lines:
            self.lines = [existing for existing in self.lines if existing != line]

        version_idx = next((i for i, ln in enumerate(self.lines) if ln.startswith("#version")), -1)
        insert_at = version_idx + 1 if version_idx >= 0 else 0
        self.lines.insert(insert_at, line)
        self._sync_patched()

    def patch_header(self) -> None:
        self._insert_after_version(self.header_line)

    def patch_includes(self) -> None:
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

        mixin = _INCLUDE_EXTRA_MIXIN_VSH if self.stage == "vsh" else _INCLUDE_EXTRA_MIXIN_FSH
        if mixin and not any(ln.strip() == mixin for ln in self.lines):
            self.lines[include_insert:include_insert] = [mixin]
            include_insert += 1

        self.lines.insert(include_insert, self.include_line)
        self._sync_patched()


    def patch_injects(self) -> None:
        if self.inject_line in self.patched:
            return

        main_pos = self.patched.find("void main")
        brace_open = self.patched.find("{", main_pos)
        if main_pos == -1 or brace_open == -1:
            return

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
        self.patch_header()
        self.patch_includes()
        self.patch_injects()
        return self.patched


def build_command(_: argparse.Namespace) -> None:
    project_root = find_project_root()
    config = load_beet_config(project_root)
    assets_root = resolve_assets_root(project_root, config)

    print(f"Using assets root: {assets_root}")
    index = NamespaceIndex.from_assets(assets_root)
    index.print_registered()
    ShaderIncludeBuilder(index=index, options=BuildOptions(assets_root=assets_root)).build()


def patch_command(args: argparse.Namespace) -> None:
    project_root = find_project_root()
    config = load_beet_config(project_root)
    assets_root = resolve_assets_root(project_root, config)
    version = args.version or resolve_mc_version(config)

    core_path = assets_root / "minecraft" / "shaders" / "core"
    core_path.mkdir(parents=True, exist_ok=True)
    print(f"Patching vanilla {version} sources into: {core_path}")

    for pipeline in _SUPPORTED_SHADER_PIPELINES:
        for stage in _SUPPORTED_SHADER_STAGES:
            url = get_vanilla_source(version, pipeline, stage)
            with urllib.request.urlopen(url) as response:
                content = response.read().decode("utf-8")

            patched_content = ShaderPatcher(content, pipeline, stage).apply()
            (core_path / f"{pipeline}.{stage}").write_text(patched_content)


def main() -> None:
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
