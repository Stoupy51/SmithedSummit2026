""" Build the StewBeet presentation walls from TEXTS.

Orchestrator: for each wall (Zone) it derives the wall's identifiers (wall.py),
collects its entity summons (summons.py) and writes its page + navigation
functions and animation helpers (pages.py, animation.py, navigation.py), all
under walls/<slug>/.

The summons collect into walls/setup and the per-wall "reset to page 0 +
refresh" into walls/reset; __init__ calls both from the load file after
clearing old entities.
"""

# Imports
from stewbeet import write_function

from .animation import write_fade_functions, write_pop_settle
from .content import TEXTS
from .navigation import write_navigation_functions
from .pages import write_openlink_function, write_page_functions, write_show_function
from .summons import summon_commands
from .wall import Wall, unique_slugs


def write_wall_functions(wall: Wall) -> None:
	""" Write every function of one wall under walls/<slug>/: the per-page swaps
	+ the show dispatcher (+ openlink on walls with links), the pop_settle and
	fade animation helpers, and the next/prev navigation. """
	write_page_functions(wall)
	write_show_function(wall)
	if wall.has_links:
		write_openlink_function(wall)
	write_pop_settle(wall)
	write_fade_functions(wall)
	write_navigation_functions(wall)


def setup_presentation_walls(ns: str) -> None:
	""" Read TEXTS and, per wall, collect its entity summons (into walls/setup) and
	write its page + navigation functions (under walls/<slug>/). walls/reset resets
	every wall to page 0 and refreshes its display; both are called from the load
	file (see __init__) after the previous entities are killed. """
	slugs: list[str] = unique_slugs(TEXTS)

	setup_blocks: list[str] = []   # one block of entity summons per wall -> walls/setup
	reset_cmds: list[str] = []     # per-wall "score 0 + show" -> walls/reset

	for index, zone in enumerate(TEXTS):
		wall: Wall = Wall(ns, index, zone, slugs[index])
		setup_blocks.append("\n".join(summon_commands(wall)))
		write_wall_functions(wall)

		# Reset this wall to page 0 and refresh it (collected into walls/reset).
		reset_cmds += [
			f"scoreboard players set {wall.holder} {wall.page_objective} 0",
			f"function {wall.function('show')}",
		]

	# Aggregate functions: all summons (one commented block per wall), and the
	# whole-board reset.
	write_function(f"{ns}:walls/setup", "\n\n".join(setup_blocks) + "\n", overwrite=True)
	write_function(f"{ns}:walls/reset",
		"# Put every wall back on its first page and refresh its display\n"
		+ "\n".join(reset_cmds) + "\n", overwrite=True)
