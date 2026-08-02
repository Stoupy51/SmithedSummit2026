""" Moving a thrown tomato and bursting it on impact.

Movement is delegated to Bookshelf's move module, the same way StoupGun throws its grenades:
`#bs.move:apply_vel` walks the velocity stored on the `bs.vel.*` objectives, resolves the
collision against real block hitboxes, and calls back into our splat function on the first hit.
"""
# Imports
from stewbeet import Mem, write_tick_file, write_versioned_function

from .constants import GRAVITY, SPLAT_PARTICLES, TOMATO_ITEM, TOMATO_TAG


# Classes
class TomatoFlight:
	""" Per tick movement, collision and the red splat. """

	@staticmethod
	def write_tick() -> None:
		""" Drive every flying tomato once per tick. """
		ns: str = Mem.ctx.project_id
		version: str = Mem.ctx.project_version

		write_tick_file(f"""
execute as @e[type=item_display, tag={ns}.{TOMATO_TAG}] at @s run function {ns}:v{version}/{TOMATO_ITEM}/tick
""")

		write_versioned_function(f"{TOMATO_ITEM}/tick", f"""
# Fall a little faster every tick
scoreboard players remove @s bs.vel.y {GRAVITY}

# Move along the velocity and splat on the first block hit
function #bs.move:apply_vel {{scale: 0.001, with: {{blocks: true, entities: false, on_collision: "function {ns}:v{version}/{TOMATO_ITEM}/splat"}}}}

# The collision callback may already have killed us
execute unless entity @s run return 0

particle minecraft:dust{{color: [0.75, 0.09, 0.09], scale: 0.8}} ~ ~ ~ 0.02 0.02 0.02 0 1 normal @a[distance=..48]

# A tomato thrown at the sky still has to die eventually
scoreboard players remove @s {ns}.{TOMATO_ITEM}.life 1
execute if score @s {ns}.{TOMATO_ITEM}.life matches ..0 run function {ns}:v{version}/{TOMATO_ITEM}/splat
""")

	@staticmethod
	def write_splat() -> None:
		""" Burst the tomato into redstone block debris and remove it. """
		write_versioned_function(f"{TOMATO_ITEM}/splat", f"""
particle minecraft:block{{block_state: "minecraft:redstone_block"}} ~ ~ ~ 0.25 0.25 0.25 0.12 {SPLAT_PARTICLES} normal @a[distance=..64]
particle minecraft:dust{{color: [0.85, 0.1, 0.1], scale: 1.4}} ~ ~ ~ 0.3 0.3 0.3 0 25 normal @a[distance=..64]
playsound minecraft:entity.slime.squish_small player @a[distance=..32] ~ ~ ~ 1 1.4
kill @s
""")

	@staticmethod
	def write() -> None:
		""" Write the movement and impact functions. """
		TomatoFlight.write_tick()
		TomatoFlight.write_splat()
