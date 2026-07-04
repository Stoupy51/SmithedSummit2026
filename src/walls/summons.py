""" Entity summons for one presentation wall (collected into walls/setup).

Each wall is made of a static title, a dynamic page text_display, two textured
nav arrows (each backed by a summit.interactable interaction) and - on walls
whose pages carry links - a centered "Open link" prompt + its interaction.
This module builds their NBT and assembles the `summon` commands.

Geometry note: offsets come from settings.py and are in the wall's local frame
(caret: ^left ^up ^forward, where "forward" is the way each Zone.rotation
faces). If a wall's text or arrows face away, or left<->right feel swapped,
flip that Zone's rotation by 180 in content.py.
"""

# Imports
from stouputils.typing import JsonDict

from ..utils.nbt import nbt, root, scale_only, with_uuid
from .links import link_hint
from .settings import (
	ARROW_OUT,
	ARROW_SCALE,
	ARROW_UP,
	INT_H,
	INT_W,
	LINK_INT,
	LINK_SCALE,
	PAGE_UP,
	TITLE_SCALE,
	TITLE_UP,
	WALL_FWD,
)
from .wall import Wall


def title_nbt(wall: Wall) -> JsonDict:
	""" NBT for the static title text_display floating above the wall. """
	return {
		"Tags": [f"{wall.ns}.wall", f"summit.booth_entity.{wall.ns}", "summit.static"], "billboard": "fixed", "alignment": "center", "Rotation": wall.rotation,
		"text": root([{"text": wall.zone.name, "bold": True, "color": "#FFD479"}]),
		"transformation": scale_only(TITLE_SCALE, TITLE_SCALE, TITLE_SCALE),
		"brightness": {"block": 15, "sky": 15},
	}


def page_nbt(wall: Wall) -> JsonDict:
	""" NBT for the dynamic page text_display, baked with page 0.

	The text is swapped on navigation; each page's text size (page.scale,
	defaulting to PAGE_SCALE) rides in the transformation scale, refreshed on
	every swap (see pages.write_page_functions). """
	first = wall.zone.pages[0]
	first_scale: float = wall.page_scale(first)
	return {
		"Tags": [f"{wall.ns}.wall", f"summit.booth_entity.{wall.ns}", "summit.dynamic"], "billboard": "fixed", "alignment": "left",
		"Rotation": wall.rotation, "line_width": first.line_width, "text": root(first.text),
		"transformation": scale_only(first_scale, first_scale, first_scale),
		"brightness": {"block": 15, "sky": 15},
	}


def arrow_nbt(wall: Wall, model: str) -> JsonDict:
	""" NBT for a nav-arrow item_display showing the `model` item model.

	Arrows are dynamic (their texture grays out at the boundaries), so they
	carry the summit.dynamic tag - not summit.static. """
	return {
		"Tags": [f"{wall.ns}.wall", f"summit.booth_entity.{wall.ns}", "summit.dynamic"], "billboard": "fixed", "item_display": "fixed", "Rotation": wall.rotation,
		"item": {"id": "stone", "count": 1, "components": {"minecraft:item_model": f"{wall.ns}:{model}"}},
		"transformation": scale_only(ARROW_SCALE, ARROW_SCALE, ARROW_SCALE),
		"brightness": {"block": 15, "sky": 15},
	}


def nav_interaction_nbt(wall: Wall, action: str) -> JsonDict:
	""" NBT for the interaction entity behind an arrow: right-click runs the
	wall's `action` function (next or prev). """
	return {
		"Tags": [f"{wall.ns}.wall", f"summit.booth_entity.{wall.ns}", "summit.static", "summit.interactable"],
		"width": INT_W, "height": INT_H, "response": True,
		"data": {"summit_interactable": {"on_right_click": f"function {wall.function(action)}"}},
	}


def link_prompt_nbt(wall: Wall) -> JsonDict:
	""" NBT for the centered "Open link" prompt, baked with page 0's links.

	Dynamic: refreshed on every page swap (empty text on linkless pages). """
	return {
		"Tags": [f"{wall.ns}.wall", f"summit.booth_entity.{wall.ns}", "summit.dynamic"], "billboard": "fixed", "alignment": "center",
		"Rotation": wall.rotation, "text": root(link_hint(wall.page_links[0])),
		"transformation": scale_only(LINK_SCALE, LINK_SCALE, LINK_SCALE),
		"brightness": {"block": 15, "sky": 15},
	}


def link_interaction_nbt(wall: Wall) -> JsonDict:
	""" NBT for the interaction entity behind the "Open link" prompt.

	Dynamic too: its hitbox shrinks to 0 on pages with no link, so it isn't
	physically there to be clicked. 'execute on target run' switches the
	executor to the player who right-clicked (summit_interactable otherwise
	runs commands as/at the interaction entity), so openlink's
	`dialog show @s` targets them. """
	first_link_size: float = LINK_INT if wall.page_links[0] else 0.0
	return {
		"Tags": [f"{wall.ns}.wall", f"summit.booth_entity.{wall.ns}", "summit.dynamic", "summit.interactable"],
		"width": first_link_size, "height": first_link_size, "response": True,
		"data": {"summit_interactable": {"on_right_click": f"execute on target run function {wall.function('openlink')}"}},
	}


def summon_commands(wall: Wall) -> list[str]:
	""" Every `summon` command for this wall, in setup order.

	The display faces the viewer, so the executor's left is the viewer's
	right: caret +left -> viewer's right (next), caret -left -> left (prev). """
	anchor: str = wall.anchor
	iy: float = ARROW_UP - INT_H / 2
	title: str = wall.zone.name.replace("\n", " ")
	commands: list[str] = [
		f"# Wall {wall.index + 1}: {title} ({wall.slug})",
		"# Title above the wall + the page text_display (baked with page 0, swapped on navigation)",
		f"execute {anchor} run summon text_display ^ ^{TITLE_UP} ^{WALL_FWD} {nbt(title_nbt(wall))}",
		f"execute {anchor} run summon text_display ^ ^{PAGE_UP} ^{WALL_FWD} {with_uuid(wall.page_uuid, page_nbt(wall))}",
		"# Nav arrows + the interactions catching their right-clicks (viewer's right = next)",
		f"execute {anchor} run summon item_display ^{ARROW_OUT} ^{ARROW_UP} ^{WALL_FWD} {with_uuid(wall.right_arrow_uuid, arrow_nbt(wall, 'nav_arrow_right'))}",
		f"execute {anchor} run summon item_display ^-{ARROW_OUT} ^{ARROW_UP} ^{WALL_FWD} {with_uuid(wall.left_arrow_uuid, arrow_nbt(wall, 'nav_arrow_left'))}",
		f"execute {anchor} run summon interaction ^{ARROW_OUT} ^{iy} ^{WALL_FWD} {nbt(nav_interaction_nbt(wall, 'next'))}",
		f"execute {anchor} run summon interaction ^-{ARROW_OUT} ^{iy} ^{WALL_FWD} {nbt(nav_interaction_nbt(wall, 'prev'))}",
	]

	# Centered "Open link" prompt + its interaction, between the two arrows.
	# Both are only worth summoning when some page on this wall carries a link.
	if wall.has_links:
		link_iy: float = ARROW_UP - LINK_INT / 2
		commands += [
			'# Centered "Open link" prompt + its interaction (some pages on this wall carry links)',
			f"execute {anchor} run summon text_display ^ ^{ARROW_UP} ^{WALL_FWD} {with_uuid(wall.link_prompt_uuid, link_prompt_nbt(wall))}",
			f"execute {anchor} run summon interaction ^ ^{link_iy} ^{WALL_FWD} {with_uuid(wall.link_interaction_uuid, link_interaction_nbt(wall))}",
		]
	return commands
