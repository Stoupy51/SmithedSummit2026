
# Imports
import json

from beet import Context
from stewbeet import *  # type: ignore

from .texts import TEXTS


# Utility functions
def scale_only(sx: float, sy: float, sz: float) -> JsonDict:
    return {
        "left_rotation":[0.0, 0.0, 0.0, 1.0],
        "right_rotation": [0.0, 0.0, 0.0, 1.0],
        "scale": [sx, sy, sz],
        "translation": [0.0, 0.0, 0.0]
    }

def item_nbt(item: str, **kwargs: Any) -> JsonDict:
    ns: str = Mem.ctx.project_id
    return {
        "item":{
            "id": "stone",
            "components": {"minecraft:item_model":f"{ns}:{item}"},
            "count": 1,
        },
        "Tags": [f"{ns}.{item}", f"{ns}.static", "summit.static"],
        "brightness": {"block": 15, "sky": 15},
        **kwargs
    }

def dump(obj: Any) -> str:
    return json.dumps(obj)[1:-1]

def nbt(obj: Any) -> str:
    """Full SNBT-compatible serialization (modern SNBT accepts this JSON form)."""
    return json.dumps(obj, ensure_ascii=False)

def root(components: Any) -> list[Any]:
    """Wrap components with an empty root so siblings don't inherit the first
    element's formatting (a bold title would otherwise bold the whole page)."""
    return ["", *components]

def with_uuid(uuid: str, obj: JsonDict) -> str:
    """SNBT for `obj` with a fixed `UUID:uuid("...")` spliced in, so the entity
    can be selected directly by UUID instead of by tag."""
    return '{UUID:uuid("' + uuid + '"),' + nbt(obj)[1:]


# ── Presentation walls ──────────────────────────────────────────────────────
# Geometry tweakables, in the wall's local frame (caret: ^left ^up ^forward,
# where "forward" is the way each Zone.rotation faces). Tune in-world as needed.
# If a wall's text/arrows face away or left<->right feel swapped, flip that
# Zone's rotation by 180 in texts.py.
WALL_FWD: float = -0.45     # push displays just in front of the wall face
PAGE_UP: float = 1.2        # page text vertical offset from the anchor block
TITLE_UP: float = 3.0       # title sits above the wall
ARROW_UP: float = 0.5       # arrows vertical offset (same height as the page)
ARROW_OUT: float = 1.0      # horizontal distance from center to each arrow
INT_W: float = 0.9          # interaction hitbox width
INT_H: float = 0.9          # interaction hitbox height
PAGE_SCALE: float = 0.65    # text_display scale for pages
TITLE_SCALE: float = 1.0    # text_display scale for the title
ARROW_SCALE: float = 1.0    # item_display scale for the arrows


def setup_presentation_walls(ns: str) -> None:
    """ Read TEXTS and place, per wall: a title, a page display, and left/right
    textured arrows each backed by a summit.interactable interaction entity.

    The page display is the only dynamic entity (its text is swapped on click),
    so it is NOT tagged summit.static; the arrows are dynamic too (their texture
    is gray out at the page boundaries), so they aren't static either.
    """
    obj: str = f"{ns}.page"
    static: list[str] = [f"{ns}.wall", "summit.static"]
    summons: list[str] = []

    for zi, zone in enumerate(TEXTS):
        x, y, z = zone.coords
        yaw: int = zone.rotation
        ax, ay, az = x + 0.5, y - 1.0, z + 0.5
        anchor: str = f"positioned {ax} {ay} {az} rotated {yaw} 0"
        rot: list[int] = [yaw, 0]
        n: int = len(zone.pages)
        first = zone.pages[0]

        # Fixed UUIDs for the three dynamic entities of this wall, so their
        # functions can target them directly (no per-tick @e tag scan).
        disp_uuid: str = f"20180612-2026-2002-2098-2020{zi:08d}"
        left_uuid: str = f"20180612-2026-2002-2098-2021{zi:08d}"
        right_uuid: str = f"20180612-2026-2002-2098-2022{zi:08d}"

        # Title (static) - above the wall.
        title_nbt: JsonDict = {
            "Tags": static, "billboard": "fixed", "alignment": "center", "Rotation": rot,
            "text": root([{"text": zone.name, "bold": True, "color": "#FFD479"}]),
            "transformation": scale_only(TITLE_SCALE, TITLE_SCALE, TITLE_SCALE),
            "brightness": {"block": 15, "sky": 15},
        }
        # Page (dynamic) - baked with page 0; swapped on navigation.
        page_nbt: JsonDict = {
            "Tags": [f"{ns}.wall"], "billboard": "fixed", "alignment": "left",
            "Rotation": rot, "line_width": first.line_width, "text": root(first.text),
            "transformation": scale_only(PAGE_SCALE, PAGE_SCALE, PAGE_SCALE),
            "brightness": {"block": 15, "sky": 15},
        }

        # Arrows are dynamic (texture gray at the boundaries), so they carry
        # only the wall tag - not summit.static.
        def arrow_nbt(model: str, rot: list[int] = rot) -> JsonDict:
            return {
                "Tags": [f"{ns}.wall"], "billboard": "fixed", "item_display": "fixed", "Rotation": rot,
                "item": {"id": "stone", "count": 1, "components": {"minecraft:item_model": f"{ns}:{model}"}},
                "transformation": scale_only(ARROW_SCALE, ARROW_SCALE, ARROW_SCALE),
                "brightness": {"block": 15, "sky": 15},
            }

        def interaction_nbt(action: str, zi: int = zi) -> JsonDict:
            return {
                "Tags": [f"{ns}.wall", "summit.static", "summit.interactable"],
                "width": INT_W, "height": INT_H, "response": True,
                "data": {"summit_interactable": {"on_right_click": f"function {ns}:walls/zone{zi}/{action}"}},
            }

        # The display faces the viewer, so the executor's left is the viewer's
        # right: caret +left -> viewer's right (next), caret -left -> left (prev).
        iy: float = ARROW_UP - INT_H / 2
        summons += [
            f"execute {anchor} run summon minecraft:text_display ^ ^{TITLE_UP} ^{WALL_FWD} {nbt(title_nbt)}",
            f"execute {anchor} run summon minecraft:text_display ^ ^{PAGE_UP} ^{WALL_FWD} {with_uuid(disp_uuid, page_nbt)}",
            f"execute {anchor} run summon minecraft:item_display ^{ARROW_OUT} ^{ARROW_UP} ^{WALL_FWD} {with_uuid(right_uuid, arrow_nbt('nav_arrow_right'))}",
            f"execute {anchor} run summon minecraft:item_display ^-{ARROW_OUT} ^{ARROW_UP} ^{WALL_FWD} {with_uuid(left_uuid, arrow_nbt('nav_arrow_left'))}",
            f"execute {anchor} run summon minecraft:interaction ^{ARROW_OUT} ^{iy} ^{WALL_FWD} {nbt(interaction_nbt('next'))}",
            f"execute {anchor} run summon minecraft:interaction ^-{ARROW_OUT} ^{iy} ^{WALL_FWD} {nbt(interaction_nbt('prev'))}",
        ]

        # One function per page: swap the page text + width, and gray out the
        # arrow that has no page beyond it (left on the first, right on the last).
        for pi, page in enumerate(zone.pages):
            left_model: str = "gray_nav_arrow_left" if pi == 0 else "nav_arrow_left"
            right_model: str = "gray_nav_arrow_right" if pi == n - 1 else "nav_arrow_right"
            write_function(f"{ns}:walls/zone{zi}/page{pi}",
                f"data modify entity {disp_uuid} text set value {nbt(root(page.text))}\n"
                f"data modify entity {disp_uuid} line_width set value {page.line_width}\n"
                f'data modify entity {left_uuid} item.components."minecraft:item_model" set value "{ns}:{left_model}"\n'
                f'data modify entity {right_uuid} item.components."minecraft:item_model" set value "{ns}:{right_model}"\n')

        # Dispatch the current page index to the matching page function.
        write_function(f"{ns}:walls/zone{zi}/show", "\n".join(
            f"execute if score #wall{zi} {obj} matches {pi} run function {ns}:walls/zone{zi}/page{pi}"
            for pi in range(n)) + "\n")

        # Navigation: advance/rewind with wrap-around, then refresh + click sound.
        write_function(f"{ns}:walls/zone{zi}/next", f"""
scoreboard players add #wall{zi} {obj} 1
execute if score #wall{zi} {obj} matches {n}.. run scoreboard players set #wall{zi} {obj} {n - 1}
function {ns}:walls/zone{zi}/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
""")
        write_function(f"{ns}:walls/zone{zi}/prev", f"""
scoreboard players remove #wall{zi} {obj} 1
execute if score #wall{zi} {obj} matches ..-1 run scoreboard players set #wall{zi} {obj} 0
function {ns}:walls/zone{zi}/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
""")

    # On load: create the objective, clear any previous wall entities, (re)spawn
    # everything, reset every wall back to its first page, then run each wall's
    # show once so the page text and arrow gray-state match page 0.
    init: str = "\n".join(f"scoreboard players set #wall{zi} {obj} 0" for zi in range(len(TEXTS)))
    show: str = "\n".join(f"function {ns}:walls/zone{zi}/show" for zi in range(len(TEXTS)))
    write_load_file(
        f"\n# Presentation walls (StewBeet)\n"
        f"scoreboard objectives add {obj} dummy\n"
        f"kill @e[tag={ns}.wall]\n"
        + "\n".join(summons) + "\n"
        + init + "\n"
        + show + "\n"
    )


# Main entry point (ran just before making finalyzing the build process (zip, headers, lang, ...))
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id  # type: ignore

    # Blackhole
    black_hole: str = "20180612-2026-2002-2098-201000000000"
    black_hole_nbt: JsonDict = item_nbt("bg_black_hole", transformation=scale_only(16.69, 9.69, -18.69))

    # Logo
    logo: str = "20180612-2026-2002-2098-201000000001"
    logo_nbt: JsonDict = item_nbt("logo", transformation=scale_only(2.5, 2.5, 4.0), Rotation=[180,0])

    # Title
    title: str = "20180612-2026-2002-2098-201000000002"
    title_nbt: JsonDict = item_nbt("title", transformation=scale_only(3.5, 3.5, 3.5), Rotation=[0,0])

    # Arrow
    arrow_1: str = "20180612-2026-2002-2098-201000000003"
    arrow_2: str = "20180612-2026-2002-2098-201000000004"
    arrow_trans_1: JsonDict = scale_only(5.0, 5.0, 5.0)
    arrow_trans_1["left_rotation"] = [0.0, 0.0, 0.172, 0.985]
    arrow_nbt_1: JsonDict = item_nbt("arrow", transformation=arrow_trans_1)
    arrow_nbt_2: JsonDict = item_nbt("arrow", transformation=scale_only(5.0, 5.0, 2.5), Rotation=[-90,0])


    # You can either write your mcfunction files in src/data/... or with the python way:
    # Add some commands when loading datapack
    write_load_file(f"""
# TODO: remove when we're all finished.
kill @e[tag={ns}.static]

# Summon a Black Hole underground
execute unless entity {black_hole} run summon minecraft:item_display 198.5 54.0 -21.5 {{UUID:uuid("{black_hole}"),{dump(black_hole_nbt)}}}

# Summon the logo, title, and arrow at entrance
execute unless entity {logo} run summon minecraft:item_display 196.5 103.5 -9.9 {{UUID:uuid("{logo}"),{dump(logo_nbt)}}}
execute unless entity {title} run summon minecraft:item_display 196.5 103.0 -9.6 {{UUID:uuid("{title}"),{dump(title_nbt)}}}
execute unless entity {arrow_1} run summon minecraft:item_display 197.6875 99.4375 -10.5 {{UUID:uuid("{arrow_1}"),{dump(arrow_nbt_1)}}}
execute unless entity {arrow_2} run summon minecraft:item_display 198.9375 98.125 -4.0 {{UUID:uuid("{arrow_2}"),{dump(arrow_nbt_2)}}}
""")

    # Place the 10 StewBeet presentation walls (read from src/texts.py).
    setup_presentation_walls(ns)

    pass

