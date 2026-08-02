
#> stoupy_panel:v1.0.0/tomato/tick
#
# @executed	as @e[type=item_display,tag=stoupy_panel.tomato] & at @s
#
# @within	stoupy_panel:v1.0.0/tick [ as @e[type=item_display,tag=stoupy_panel.tomato] & at @s ]
#

# Fall a little faster every tick
scoreboard players remove @s bs.vel.y 35

# Move along the velocity and splat on the first block hit
function #bs.move:apply_vel {scale: 0.001, with: {blocks: true, entities: false, on_collision: "function stoupy_panel:v1.0.0/tomato/splat"}}

# The collision callback may already have killed us
execute unless entity @s run return 0

particle minecraft:dust{color: [0.75, 0.09, 0.09], scale: 0.8} ~ ~ ~ 0.02 0.02 0.02 0 1 normal @a[distance=..48]

# A tomato thrown at the sky still has to die eventually
scoreboard players remove @s stoupy_panel.tomato.life 1
execute if score @s stoupy_panel.tomato.life matches ..0 run function stoupy_panel:v1.0.0/tomato/splat

