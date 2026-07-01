""" Build the StewBeet presentation walls from TEXTS.

Per wall (Zone) this summons a title, a page display and left/right textured nav
arrows (each backed by a summit.interactable interaction), plus - on walls whose
pages carry links - a centered "Open link" prompt + interaction. It also writes,
per wall, one function per page (swap text/scale + gray the boundary arrow) and
show / next / prev (+ openlink) navigation, all under walls/<slug>/.

The summons collect into walls/setup and the per-wall "reset to page 0 + refresh"
into walls/reset; __init__ calls both from the load file after clearing old entities.

Geometry note: constants below are in the wall's local frame (caret: ^left ^up
^forward, where "forward" is the way each Zone.rotation faces). If a wall's text or
arrows face away, or left<->right feel swapped, flip that Zone's rotation by 180 in
content.py.
"""

# Imports
import re

from stewbeet import write_function
from stouputils.typing import JsonDict

from ..utils.nbt import nbt, root, scale_only, with_uuid
from .content import TEXTS, Zone
from .links import collect_links, link_dialog, link_hint

# ── Geometry tweakables (tune in-world as needed) ────────────────────────────
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


def zone_slug(name: str) -> str:
	""" Filesystem-friendly folder name for a zone, from its title
	(e.g. 'Recipes & Loot' -> 'recipes_loot'). """
	return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")

def _unique_slugs(zones: list[Zone]) -> list[str]:
	""" zone_slug for each zone, disambiguating any collision with a numeric suffix. """
	slugs: list[str] = []
	for zi, zone in enumerate(zones):
		slug: str = zone_slug(zone.name)
		if slug in slugs:
			slug = f"{slug}_{zi}"
		slugs.append(slug)
	return slugs


def setup_presentation_walls(ns: str) -> None:
	""" Read TEXTS and, per wall, collect its entity summons (into walls/setup) and
	write its page + navigation functions (under walls/<slug>/). walls/reset resets
	every wall to page 0 and refreshes its display; both are called from the load
	file (see __init__) after the previous entities are killed. """
	obj: str = f"{ns}.page"
	static: list[str] = [f"{ns}.wall", "summit.static"]
	slugs: list[str] = _unique_slugs(TEXTS)

	setup_cmds: list[str] = []   # entity summons -> walls/setup
	reset_cmds: list[str] = []   # per-wall "score 0 + show" -> walls/reset

	for zi, zone in enumerate(TEXTS):
		slug: str = slugs[zi]
		base: str = f"{ns}:walls/{slug}"   # function-path prefix for this wall
		holder: str = f"#{slug}"           # scoreboard fake-player holding the page index

		x, y, z = zone.coords
		yaw: int = zone.rotation
		ax, ay, az = x + 0.5, y - 1.0, z + 0.5
		anchor: str = f"positioned {ax} {ay} {az} rotated {yaw} 0"
		rot: list[int] = [yaw, 0]
		n: int = len(zone.pages)
		first = zone.pages[0]

		# Fixed UUIDs for this wall's dynamic entities (page, both arrows and, on
		# walls with links, the "Open link" prompt + its interaction), so the page
		# functions target them directly (no per-tick @e tag scan).
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

		def interaction_nbt(action: str, base: str = base) -> JsonDict:
			return {
				"Tags": [f"{ns}.wall", "summit.static", "summit.interactable"],
				"width": INT_W, "height": INT_H, "response": True,
				"data": {"summit_interactable": {"on_right_click": f"function {base}/{action}"}},
			}

		# The display faces the viewer, so the executor's left is the viewer's
		# right: caret +left -> viewer's right (next), caret -left -> left (prev).
		iy: float = ARROW_UP - INT_H / 2
		setup_cmds += [
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
				"data": {"summit_interactable": {"on_right_click": f"execute on target run function {base}/openlink"}},
			}
			link_iy: float = ARROW_UP - LINK_INT / 2
			setup_cmds += [
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
			write_function(f"{base}/page_{pi}", f"""
data modify entity {disp_uuid} text set value {nbt(root(page.text))}
data modify entity {disp_uuid} line_width set value {page.line_width}
data modify entity {disp_uuid} transformation.scale set value {nbt([page_scale, page_scale, page_scale])}
data modify entity {left_uuid} item.components."minecraft:item_model" set value "{ns}:{left_model}"
data modify entity {right_uuid} item.components."minecraft:item_model" set value "{ns}:{right_model}"
{link_lines}
""", overwrite=True)

		# Dispatch the current page index to the matching page function.
		write_function(f"{base}/show", "\n".join(
			f"execute if score {holder} {obj} matches {pi} run function {base}/page_{pi}"
			for pi in range(n)) + "\n", overwrite=True)

		# Open the current page's link dialog (only pages that have links get a
		# branch; on a linkless page the centered interaction has a 0-size hitbox).
		# The dialog is inlined into the command (SNBT) rather than registered as a
		# data-pack file, so it works without a server restart. @s is the clicking
		# player thanks to the 'execute on target run' in the interaction's callback.
		if has_links:
			write_function(f"{base}/openlink", "\n".join(
				f"execute if score {holder} {obj} matches {pi} run dialog show @s {nbt(link_dialog(zone.name, zone.pages[pi].name, links))}"
				for pi, links in enumerate(zone_links) if links) + "\n", overwrite=True)

		# Navigation: advance/rewind with wrap-around, then refresh + click sound.
		write_function(f"{base}/next", f"""
scoreboard players add {holder} {obj} 1
execute if score {holder} {obj} matches {n}.. run scoreboard players set {holder} {obj} {n - 1}
function {base}/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
""", overwrite=True)
		write_function(f"{base}/prev", f"""
scoreboard players remove {holder} {obj} 1
execute if score {holder} {obj} matches ..-1 run scoreboard players set {holder} {obj} 0
function {base}/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
""", overwrite=True)

		# Reset this wall to page 0 and refresh it (collected into walls/reset).
		reset_cmds += [f"scoreboard players set {holder} {obj} 0", f"function {base}/show"]

	# Aggregate functions: all summons, and the whole-board reset.
	write_function(f"{ns}:walls/setup", "\n".join(setup_cmds) + "\n", overwrite=True)
	write_function(f"{ns}:walls/reset", "\n".join(reset_cmds) + "\n", overwrite=True)
