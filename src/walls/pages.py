""" Per-page functions for one wall: page_<i>, show and openlink.

page_<i> swaps the page text / width / scale into the dynamic display and grays
the boundary arrow; show dispatches the current page-index score to the matching
page_<i>; openlink opens the current page's link dialog.
"""

# Imports
from stewbeet import write_function

from ..utils.nbt import nbt, root
from .links import link_dialog, link_hint
from .settings import LINK_INT
from .wall import Wall


def link_refresh_lines(wall: Wall, page_index: int) -> str:
	""" Commands refreshing the centered "Open link" prompt + its interaction for
	a page: empty text + a 0-size (unclickable) hitbox when the page has no link.
	Empty string on walls that have no link entity at all. """
	if not wall.has_links:
		return ""
	link_size: float = LINK_INT if wall.page_links[page_index] else 0.0
	return f"""
data modify entity {wall.link_prompt_uuid} text set value {nbt(root(link_hint(wall.page_links[page_index])))}
data modify entity {wall.link_interaction_uuid} width set value {link_size}f
data modify entity {wall.link_interaction_uuid} height set value {link_size}f
"""


def write_page_functions(wall: Wall) -> None:
	""" Write one function per page: swap the page text + width + scale, and gray
	out the arrow that has no page beyond it (left on the first, right on the last). """
	for pi, page in enumerate(wall.zone.pages):
		left_model: str = "gray_nav_arrow_left" if pi == 0 else "nav_arrow_left"
		right_model: str = "gray_nav_arrow_right" if pi == wall.page_count - 1 else "nav_arrow_right"
		page_scale: float = wall.page_scale(page)
		write_function(wall.function(f"page_{pi}"), f"""
data modify entity {wall.page_uuid} text set value {nbt(root(page.text))}
data modify entity {wall.page_uuid} line_width set value {page.line_width}
data modify entity {wall.page_uuid} transformation.scale set value [{page_scale}f, {page_scale}f, {page_scale}f]
data modify entity {wall.left_arrow_uuid} item.components."minecraft:item_model" set value "{wall.ns}:{left_model}"
data modify entity {wall.right_arrow_uuid} item.components."minecraft:item_model" set value "{wall.ns}:{right_model}"
{link_refresh_lines(wall, pi)}
""", overwrite=True)


def write_show_function(wall: Wall) -> None:
	""" Write show: dispatch the current page-index score to the matching page function. """
	write_function(wall.function("show"), "\n".join(
		f"execute if score {wall.holder} {wall.page_objective} matches {pi} run function {wall.function(f'page_{pi}')}"
		for pi in range(wall.page_count)) + "\n", overwrite=True)


def write_openlink_function(wall: Wall) -> None:
	""" Write openlink: open the current page's link dialog.

	Only pages that have links get a branch; on a linkless page the centered
	interaction has a 0-size hitbox so this can't fire. The dialog is inlined
	into the command (SNBT) rather than registered as a data-pack file, so it
	works without a server restart. @s is the clicking player thanks to the
	'execute on target run' in the interaction's callback. """
	write_function(wall.function("openlink"), "\n".join(
		f"execute if score {wall.holder} {wall.page_objective} matches {pi} run dialog show @s {nbt(link_dialog(wall.zone.name, wall.zone.pages[pi].name, links))}"
		for pi, links in enumerate(wall.page_links) if links) + "\n", overwrite=True)
