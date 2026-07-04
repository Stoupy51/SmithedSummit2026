""" StewBeet Summit 2026 - booth entity lifecycle plugin.

beet pipeline entry (referenced as `src.booth` in beet.yml). Every entity of
this booth is function-summoned (none ride in the schematic - they all use
scores, fixed UUIDs or dynamic NBT swaps), so per the summit guidelines their
summon/kill must be exposed through the booth function tags:
    #summit.booth:<namespace>/entities/summon
    #summit.booth:<namespace>/entities/kill
This writes both functions and registers them in those tags. The booth
metadata itself (bounding boxes, stickers, balloon) lives in booth.json at the
project root, submitted alongside the packs.
"""

# Imports
from beet import Context
from stewbeet import Mem, write_function


def beet_default(ctx: Context) -> None:
	""" Write entities/summon + entities/kill and register them in the summit booth tags. """
	ns: str = Mem.ctx.project_id

	# Kill everything the booth ever summoned (every entity carries the tag).
	write_function(f"{ns}:entities/kill", f"""
kill @e[tag=summit.booth_entity.{ns}]
""", tags=[f"summit.booth:{ns}/entities/kill"])

	# Summon everything. Kill first so the call is idempotent: the load file
	# already places the entities on /reload, and the wall titles/interactions
	# have no UUID guard, so a bare re-summon would stack them.
	write_function(f"{ns}:entities/summon", f"""
# Clear any previous booth entities so repeated calls never stack
function {ns}:entities/kill

# Entrance decorations + presentation walls (reset back on page 0)
scoreboard objectives add {ns}.page dummy
function {ns}:intro/setup
function {ns}:walls/setup
function {ns}:walls/reset
""", tags=[f"summit.booth:{ns}/entities/summon"])

