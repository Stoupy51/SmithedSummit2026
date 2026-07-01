
# Imports
import json
from typing import Any, cast

from beet import Context
from stewbeet import *  # type: ignore

from .texts import TEXTS, icon_for_url, social_icon


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


# ── Links -> clickable dialogs ───────────────────────────────────────────────
# text_display entities don't fire click events in-world, so every page that
# contains a link() gets a dialog: a centered interaction between the nav arrows
# opens it, and inside, each link is a real button that opens the URL in a browser.

def collect_links(node: Any) -> list[tuple[str, str]]:
    """ Walk a text component (nested lists included) and return every (label, url)
    pair carried by an open_url click_event, in reading order."""
    found: list[tuple[str, str]] = []
    if isinstance(node, list):
        for child in node:  # type: ignore[reportUnknownVariableType]
            found += collect_links(child)
    elif isinstance(node, dict):
        component = cast(dict[str, Any], node)
        event = component.get("click_event")
        if isinstance(event, dict):
            event = cast(dict[str, Any], event)
            if event.get("action") == "open_url":
                url: str = str(event.get("url", ""))
                found.append((str(component.get("text", url)), url))
    return found

def link_button_label(label: str, url: str) -> TextComponent:
    """ Dialog button label: the platform icon (when known) followed by the text.
    Starts with an empty parent so the icon's custom font doesn't leak onto the
    label (in a component list, siblings inherit from the first element)."""
    text: JsonDict = {"text": label, "color": "#8BE9FD"}
    key: str | None = icon_for_url(url)
    return ["", social_icon(key), {"text": " "}, text] if key else [text]

def link_dialog(title: str, subtitle: str, links: list[tuple[str, str]]) -> JsonDict:
    """A multi_action dialog with one open_url button per link on the page."""
    return {
        "type": "minecraft:multi_action",
        "title": {"text": title, "bold": True, "color": "#FFD479"},
        "body": [{
            "type": "minecraft:plain_message", "width": 240,
            "contents": {"text": subtitle, "color": "gray"},
        }],
        "columns": 1,
        "actions": [{
            "label": link_button_label(label, url),
            "tooltip": {"text": url, "color": "gray"},
            "width": 240,
            "action": {"type": "open_url", "url": url},
        } for label, url in links],
        "exit_action": {"label": {"text": "Close", "color": "red"}},
        "can_close_with_escape": True,
    }

def link_hint(links: list[tuple[str, str]]) -> list[JsonDict]:
    """The centered under-arrows prompt: platform icon + 'Open link' when the page
    has a link (with a '+N' when it has several), otherwise nothing."""
    if not links:
        return [{"text": ""}]
    key: str | None = icon_for_url(links[0][1])
    parts: list[JsonDict] = [social_icon(key), {"text": " "}] if key else []
    parts.append({"text": "Open link", "color": "#8BE9FD", "underlined": True})
    if len(links) > 1:
        parts.append({"text": f" (+{len(links) - 1})", "color": "gray"})
    return parts


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
PAGE_SCALE: float = 0.60    # text_display scale for pages
TITLE_SCALE: float = 0.9    # text_display scale for the title
ARROW_SCALE: float = 1.0    # item_display scale for the arrows
LINK_SCALE: float = 0.5     # text_display scale for the centered "Open link" prompt
LINK_INT: float = 0.75      # "Open link" interaction hitbox size (0 on pages with no link)


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

        # Fixed UUIDs for the dynamic entities of this wall (page, both arrows and,
        # on walls with links, the "Open link" prompt), so their functions can
        # target them directly (no per-tick @e tag scan).
        disp_uuid: str = f"20180612-2026-2002-2098-2020{zi:08d}"
        left_uuid: str = f"20180612-2026-2002-2098-2021{zi:08d}"
        right_uuid: str = f"20180612-2026-2002-2098-2022{zi:08d}"
        link_uuid: str = f"20180612-2026-2002-2098-2023{zi:08d}"
        link_int_uuid: str = f"20180612-2026-2002-2098-2024{zi:08d}"

        # Links present on each page (empty list = none). A wall gets its centered
        # "Open link" prompt + interaction only when at least one page has a link.
        zone_links: list[list[tuple[str, str]]] = [collect_links(p.text) for p in zone.pages]
        has_links: bool = any(zone_links)

        # Title (static) - above the wall.
        title_nbt: JsonDict = {
            "Tags": static, "billboard": "fixed", "alignment": "center", "Rotation": rot,
            "text": root([{"text": zone.name, "bold": True, "color": "#FFD479"}]),
            "transformation": scale_only(TITLE_SCALE, TITLE_SCALE, TITLE_SCALE),
            "brightness": {"block": 15, "sky": 15},
        }
        # Page (dynamic) - baked with page 0; swapped on navigation. Each page's
        # text size (page.scale, defaulting to PAGE_SCALE) rides in the
        # transformation scale, refreshed on every swap (see the per-page function).
        first_scale: float = first.scale if first.scale is not None else PAGE_SCALE
        page_nbt: JsonDict = {
            "Tags": [f"{ns}.wall", "summit.dynamic"], "billboard": "fixed", "alignment": "left",
            "Rotation": rot, "line_width": first.line_width, "text": root(first.text),
            "transformation": scale_only(first_scale, first_scale, first_scale),
            "brightness": {"block": 15, "sky": 15},
        }

        # Arrows are dynamic (texture gray at the boundaries), so they carry
        # only the wall tag - not summit.static.
        def arrow_nbt(model: str, rot: list[int] = rot) -> JsonDict:
            return {
                "Tags": [f"{ns}.wall", "summit.dynamic"], "billboard": "fixed", "item_display": "fixed", "Rotation": rot,
                "item": {"id": "stone", "count": 1, "components": {"minecraft:item_model": f"{ns}:{model}"}},
                "transformation": scale_only(ARROW_SCALE, ARROW_SCALE, ARROW_SCALE),
                "brightness": {"block": 15, "sky": 15},
            }

        def interaction_nbt(action: str, zi: int = zi) -> JsonDict:
            return {
                "Tags": [f"{ns}.wall", "summit.static", "summit.interactable"],
                "width": INT_W, "height": INT_H, "response": True,
                "data": {"summit_interactable": {"on_right_click": f"function {ns}:walls/zone_{zi}/{action}"}},
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

        # Centered "Open link" prompt + its interaction, between the two arrows.
        # Both are only worth summoning when some page on this wall carries a link;
        # the prompt (dynamic) is baked with page 0 and refreshed on every swap. The
        # interaction is a dynamic entity too: its hitbox shrinks to 0 on pages with
        # no link, so it isn't physically there to be clicked (see the page loop).
        if has_links:
            link_hint_nbt: JsonDict = {
                "Tags": [f"{ns}.wall", "summit.dynamic"], "billboard": "fixed", "alignment": "center",
                "Rotation": rot, "text": root(link_hint(zone_links[0])),
                "transformation": scale_only(LINK_SCALE, LINK_SCALE, LINK_SCALE),
                "brightness": {"block": 15, "sky": 15},
            }
            first_link_size: float = LINK_INT if zone_links[0] else 0.0
            # 'execute on target run' switches the executor to the player who
            # right-clicked (summit_interactable otherwise runs commands as/at the
            # interaction entity), so openlink's `dialog show @s` targets them.
            link_int_nbt: JsonDict = {
                "Tags": [f"{ns}.wall", "summit.static", "summit.interactable"],
                "width": first_link_size, "height": first_link_size, "response": True,
                "data": {"summit_interactable": {"on_right_click": f"execute on target run function {ns}:walls/zone_{zi}/openlink"}},
            }
            link_iy: float = ARROW_UP - LINK_INT / 2
            summons += [
                f"execute {anchor} run summon minecraft:text_display ^ ^{ARROW_UP} ^{WALL_FWD} {with_uuid(link_uuid, link_hint_nbt)}",
                f"execute {anchor} run summon minecraft:interaction ^ ^{link_iy} ^{WALL_FWD} {with_uuid(link_int_uuid, link_int_nbt)}",
            ]

        # One function per page: swap the page text + width, and gray out the
        # arrow that has no page beyond it (left on the first, right on the last).
        for pi, page in enumerate(zone.pages):
            left_model: str = "gray_nav_arrow_left" if pi == 0 else "nav_arrow_left"
            right_model: str = "gray_nav_arrow_right" if pi == n - 1 else "nav_arrow_right"
            page_scale: float = page.scale if page.scale is not None else PAGE_SCALE
            # Refresh the centered "Open link" prompt and its interaction for this
            # page: empty text + a 0-size (unclickable) hitbox when the page has no
            # link. Only emitted when the wall has a link entity at all.
            link_lines: str = ""
            if has_links:
                link_size: float = LINK_INT if zone_links[pi] else 0.0
                link_lines = f"""
data modify entity {link_uuid} text set value {nbt(root(link_hint(zone_links[pi])))}
data modify entity {link_int_uuid} width set value {link_size}f
data modify entity {link_int_uuid} height set value {link_size}f
"""
            write_function(f"{ns}:walls/zone_{zi}/page_{pi}", f"""
data modify entity {disp_uuid} text set value {nbt(root(page.text))}
data modify entity {disp_uuid} line_width set value {page.line_width}
data modify entity {disp_uuid} transformation.scale set value {nbt([page_scale, page_scale, page_scale])}
data modify entity {left_uuid} item.components."minecraft:item_model" set value "{ns}:{left_model}"
data modify entity {right_uuid} item.components."minecraft:item_model" set value "{ns}:{right_model}"
{link_lines}
""")

        # Dispatch the current page index to the matching page function.
        write_function(f"{ns}:walls/zone_{zi}/show", "\n".join(
            f"execute if score #wall{zi} {obj} matches {pi} run function {ns}:walls/zone_{zi}/page_{pi}"
            for pi in range(n)) + "\n")

        # Open the current page's link dialog (only pages that have links get a
        # branch; on a linkless page the centered interaction has a 0-size hitbox).
        # The dialog is inlined into the command (SNBT) rather than registered as a
        # data-pack file, so it works without a server restart. @s is the clicking
        # player thanks to the 'execute on target run' in the interaction's callback.
        if has_links:
            write_function(f"{ns}:walls/zone_{zi}/openlink", "\n".join(
                f"execute if score #wall{zi} {obj} matches {pi} run dialog show @s {nbt(link_dialog(zone.name, zone.pages[pi].name, links))}"
                for pi, links in enumerate(zone_links) if links) + "\n")

        # Navigation: advance/rewind with wrap-around, then refresh + click sound.
        write_function(f"{ns}:walls/zone_{zi}/next", f"""
scoreboard players add #wall{zi} {obj} 1
execute if score #wall{zi} {obj} matches {n}.. run scoreboard players set #wall{zi} {obj} {n - 1}
function {ns}:walls/zone_{zi}/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
""")
        write_function(f"{ns}:walls/zone_{zi}/prev", f"""
scoreboard players remove #wall{zi} {obj} 1
execute if score #wall{zi} {obj} matches ..-1 run scoreboard players set #wall{zi} {obj} 0
function {ns}:walls/zone_{zi}/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
""")

    # On load: create the objective, clear any previous wall entities, (re)spawn
    # everything, reset every wall back to its first page, then run each wall's
    # show once so the page text and arrow gray-state match page 0.
    init: str = "\n".join(f"scoreboard players set #wall{zi} {obj} 0" for zi in range(len(TEXTS)))
    show: str = "\n".join(f"function {ns}:walls/zone_{zi}/show" for zi in range(len(TEXTS)))
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

