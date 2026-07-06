""" StewBeet Summit 2026 - booth entity lifecycle plugin.

beet pipeline entry (referenced as `src.booth` in beet.yml, after src.intro and
src.walls). Every entity of this booth is function-summoned (none ride in the
schematic - they all use scores, fixed UUIDs or dynamic NBT swaps), so per the
summit guidelines their summon/kill must be exposed through the booth function
tags:
    #summit.booth:<namespace>/entities/summon
    #summit.booth:<namespace>/entities/kill
This writes both functions, registers them in those tags, and wires the single
load-file entry that (re)creates everything on /reload. It also writes
booth/on_enter (referenced by booth.json's on_player_enter) which rewards the
"visit the booth" sticker and, when the entering player is alone in the booth,
resets every wall to its first page; the per-wall stickers are granted from the walls'
navigation (see src/walls/navigation.py). The booth metadata itself (bounding
boxes, stickers, balloon) lives in booth.json at the project root, submitted
alongside the packs.
"""

# Imports
from stewbeet import Context, Mem, write_function, write_load_file


def beet_default(ctx: Context) -> None:
	""" Write entities/summon + entities/kill (registered in the summit booth
	tags), the load-file entry that runs them, and the booth-enter sticker grant. """
	ns: str = Mem.ctx.project_id

	# Kill everything the booth ever summoned (every entity carries the tag).
	# Living entities (the mannequin) linger ~20 ticks after /kill playing their
	# death animation; fast-forwarding DeathTime removes the corpse (and frees its
	# UUID) on the very next tick instead.
	write_function(f"{ns}:entities/kill", f"""
execute as @e[type=mannequin,tag=summit.booth_entity.{ns}] run data merge entity @s {{DeathTime: 19s}}
kill @e[tag=summit.booth_entity.{ns}]
""", tags=[f"summit.booth:{ns}/entities/kill"])

	# Summon everything. Kill first so the call is idempotent: the load file
	# also places the entities on /reload, and the wall titles/interactions
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

	# Load: (re)create every booth entity (entrance decorations + walls).
	write_load_file(f"""
# Booth entities (StewBeet): entrance decorations + presentation walls
function {ns}:entities/summon
""")

	# Runs as/at a player entering the booth (booth.json on_player_enter):
	# reward the "visit the booth" sticker (a no-op if already obtained), and if
	# they are the only player inside, put every wall back on its first page.
	write_function(f"{ns}:booth/on_enter", f"""
advancement grant @s only summit.sticker_book:{ns}/stewbeet

# Alone in the booth (the summit tags players inside with summit.in_booth.<ns>):
# reset every presentation wall to page 0 for a fresh visit
execute store result score #in_booth {ns}.data if entity @a[tag=summit.in_booth.{ns}]
execute if score #in_booth {ns}.data matches ..1 run function {ns}:walls/reset
""")

