""" Detecting the right click on a tomato and launching it.

The tomato item carries a `consumable` component only so that using it is detectable: the
`using_item` advancement fires every tick while the button is held, and a debounce tag turns
that stream back into one throw per press. The consume never completes, so no tomato is eaten.
"""
# Imports
from stewbeet import Mem, write_advancement, write_tick_file, write_versioned_function

from .constants import (
	LIFETIME,
	THROW_SPEED,
	THROWER_TAG,
	TOMATO_ITEM,
	TOMATO_TAG,
	USED_TAG,
)


# Classes
class TomatoThrow:
	""" Right click detection and the launch itself. """

	@staticmethod
	def write_use_detection() -> None:
		""" Grant an advancement while a tomato is being used, and turn it into a single throw. """
		ns: str = Mem.ctx.project_id
		version: str = Mem.ctx.project_version

		write_advancement(f"{ns}:{TOMATO_ITEM}/use", {
			"criteria": {
				"use_item": {
					"trigger": "minecraft:using_item",
					"conditions": {"item": {"predicates": {"custom_data": {ns: {TOMATO_ITEM: True}}}}},
				}
			},
			"rewards": {"function": f"{ns}:v{version}/{TOMATO_ITEM}/on_use"},
		})

		# Releasing the button revokes the advancement, which is what clears the debounce tag
		write_tick_file(f"""
tag @a[advancements={{{ns}:{TOMATO_ITEM}/use=false}},tag={ns}.{USED_TAG}] remove {ns}.{USED_TAG}
advancement revoke @a only {ns}:{TOMATO_ITEM}/use
""")

		write_versioned_function(f"{TOMATO_ITEM}/on_use", f"""
# One throw per press, not one per tick spent holding the button
execute if entity @s[tag={ns}.{USED_TAG}] run return 0
tag @s add {ns}.{USED_TAG}

function {ns}:v{version}/{TOMATO_ITEM}/throw
""")

	@staticmethod
	def write_launch() -> None:
		""" Summon the tomato at the thrower's eyes and give it the look direction as velocity. """
		ns: str = Mem.ctx.project_id
		version: str = Mem.ctx.project_version

		write_versioned_function(f"{TOMATO_ITEM}/throw", f"""
# Let the freshly summoned tomato copy the item it was thrown with
tag @s add {ns}.{THROWER_TAG}
execute anchored eyes positioned ^ ^ ^0.4 summon item_display run function {ns}:v{version}/{TOMATO_ITEM}/init
tag @s remove {ns}.{THROWER_TAG}

# Spend one tomato from the stack
item modify entity @s weapon.mainhand {ns}:v{version}/{TOMATO_ITEM}/consume_one
playsound minecraft:entity.snowball.throw player @a[distance=..24] ~ ~ ~ 0.8 1.4
""")

		write_versioned_function(f"{TOMATO_ITEM}/init", f"""
tag @s add {ns}.{TOMATO_TAG}

# Wear the exact item that was thrown, so restyling the tomato needs no change here
data modify entity @s item set from entity @n[type=player,tag={ns}.{THROWER_TAG},limit=1] equipment.mainhand
data modify entity @s item.count set value 1
data modify entity @s item_display set value "fixed"
data modify entity @s brightness set value {{sky: 15, block: 15}}
data modify entity @s teleport_duration set value 1
data modify entity @s transformation.scale set value [0.55f, 0.55f, 0.55f]

# A tomato thrown at the sky still has to die eventually
scoreboard players set @s {ns}.{TOMATO_ITEM}.life {LIFETIME}

function {ns}:v{version}/{TOMATO_ITEM}/velocity
""")

		# Reads the look direction as a unit vector, scales it to THROW_SPEED, then comes back
		write_versioned_function(f"{TOMATO_ITEM}/velocity", f"""
# Remember where we are, because reading the look vector means standing on the world origin
execute store result score #tomato.x {ns}.data run data get entity @s Pos[0] 1000
execute store result score #tomato.y {ns}.data run data get entity @s Pos[1] 1000
execute store result score #tomato.z {ns}.data run data get entity @s Pos[2] 1000

# One block forward from the origin is exactly the look direction
execute positioned 0.0 0.0 0.0 positioned ^ ^ ^1 run tp @s ~ ~ ~
execute store result score @s bs.vel.x run data get entity @s Pos[0] 1000
execute store result score @s bs.vel.y run data get entity @s Pos[1] 1000
execute store result score @s bs.vel.z run data get entity @s Pos[2] 1000

# Scale that unit vector up to the throwing speed
scoreboard players operation @s bs.vel.x *= #{THROW_SPEED} {ns}.data
scoreboard players operation @s bs.vel.y *= #{THROW_SPEED} {ns}.data
scoreboard players operation @s bs.vel.z *= #{THROW_SPEED} {ns}.data
scoreboard players operation @s bs.vel.x /= #1000 {ns}.data
scoreboard players operation @s bs.vel.y /= #1000 {ns}.data
scoreboard players operation @s bs.vel.z /= #1000 {ns}.data

# Back to the thrower's eyes
execute store result storage {ns}:temp tomato_pos.x double 0.001 run scoreboard players get #tomato.x {ns}.data
execute store result storage {ns}:temp tomato_pos.y double 0.001 run scoreboard players get #tomato.y {ns}.data
execute store result storage {ns}:temp tomato_pos.z double 0.001 run scoreboard players get #tomato.z {ns}.data
function {ns}:v{version}/{TOMATO_ITEM}/teleport_back with storage {ns}:temp tomato_pos
""")

		write_versioned_function(f"{TOMATO_ITEM}/teleport_back", "$tp @s $(x) $(y) $(z)\n")

	@staticmethod
	def write() -> None:
		""" Write every function taking a tomato from a right click to a launched entity. """
		TomatoThrow.write_use_detection()
		TomatoThrow.write_launch()
