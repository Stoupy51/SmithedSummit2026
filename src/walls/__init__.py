""" StewBeet Summit 2026 - presentation walls plugin.

beet pipeline entry (referenced as `src.walls` in beet.yml). Builds the 10
presentation walls from the content in content.py, then wires the load file to
(re)create them on every load. The entrance decorations live in their own plugin
(src/intro.py); shared NBT helpers live in src/utils.

Module map:
  content.py   Page/Zone dataclasses + the TEXTS content
  format.py    text stylers (title/body/hl/code/note/brand/beet)
  links.py     link() + the click-to-open dialog subsystem
  builder.py   setup_presentation_walls -> walls/<slug>/* + walls/setup + walls/reset
"""

# Imports
from beet import Context
from stewbeet import Mem, write_load_file

from .builder import setup_presentation_walls


# Main entry point (runs before the build is finalized: zip, headers, lang, ...).
def beet_default(ctx: Context) -> None:
	ns: str = Mem.ctx.project_id

	setup_presentation_walls(ns)

	# Load: (re)create the walls on each load. The kill clears the previous wall
	# entities so summons never stack; walls/setup runs right after it, and
	# walls/reset puts every wall back on page 0.
	# TODO: drop the kill when the summit build is finalized.
	write_load_file(f"""
# Presentation walls (StewBeet)
scoreboard objectives add {ns}.page dummy
kill @e[tag={ns}.wall]
function {ns}:walls/setup
function {ns}:walls/reset
""")
