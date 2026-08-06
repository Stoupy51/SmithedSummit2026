
#> stoupy:v1.0.0/tomato/splat
#
# @executed	as @e[type=item_display,tag=stoupy.tomato] & at @s
#
# @within	stoupy:v1.0.0/tomato/tick {scale: 0.001, with: {blocks: true, entities: false, on_collision: "function stoupy:v1.0.0/tomato/splat"}}
#			stoupy:v1.0.0/tomato/tick
#			stoupy:v1.0.0/tomato/clear [ as @e[type=item_display,tag=stoupy.tomato] & at @s ]
#

particle minecraft:block{block_state: "minecraft:redstone_block"} ~ ~ ~ 0.25 0.25 0.25 0.12 60 force @a[distance=..64]
particle minecraft:dust{color: [0.85, 0.1, 0.1], scale: 1.4} ~ ~ ~ 0.3 0.3 0.3 0 25 force @a[distance=..64]
playsound minecraft:entity.slime.squish_small player @a[distance=..32] ~ ~ ~ 1 1.4
kill @s

