""" StewBeet Summit 2026 - presentation walls plugin.

beet pipeline entry (referenced as `src.walls` in beet.yml). Builds the 10
presentation walls from the content in content.py; they are (re)created by
entities/summon (src/booth.py). The entrance decorations live in their own
plugin (src/intro.py); shared NBT helpers live in src/utils.

Module map:
    content.py     Page/Zone dataclasses + the TEXTS content
    format.py      text stylers (title/body/hl/code/note/brand/beet)
    links.py       link() + the click-to-open dialog subsystem
    settings.py    tunable geometry / scale / animation constants
    wall.py        zone_slug/unique_slugs + the per-wall Wall identifiers
    summons.py     entity NBT + the summon commands -> walls/setup
    pages.py       page_<i> / show / openlink writers
    animation.py   arrow pop + page fade writers
    navigation.py  next / prev writers
    builder.py     setup_presentation_walls -> walls/<slug>/* + walls/setup + walls/reset
"""

# Imports
import stouputils as stp
from beet import Context
from stewbeet import Mem

from .builder import setup_presentation_walls


# Main entry point (runs before the build is finalized: zip, headers, lang, ...).
@stp.measure_time(message="src.walls")
def beet_default(ctx: Context) -> None:
	""" Build the presentation walls ((re)created by entities/summon, see src/booth.py). """
	setup_presentation_walls(Mem.ctx.project_id)

