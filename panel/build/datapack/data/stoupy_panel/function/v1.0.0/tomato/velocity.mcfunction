
#> stoupy_panel:v1.0.0/tomato/velocity
#
# @executed	anchored eyes & positioned ^ ^ ^0.4
#
# @within	stoupy_panel:v1.0.0/tomato/init
#

# Remember where we are, because reading the look vector means standing on the world origin
execute store result score #tomato.x stoupy_panel.data run data get entity @s Pos[0] 1000
execute store result score #tomato.y stoupy_panel.data run data get entity @s Pos[1] 1000
execute store result score #tomato.z stoupy_panel.data run data get entity @s Pos[2] 1000

# One block forward from the origin is exactly the look direction
execute positioned 0.0 0.0 0.0 positioned ^ ^ ^1 run tp @s ~ ~ ~
execute store result score @s bs.vel.x run data get entity @s Pos[0] 1000
execute store result score @s bs.vel.y run data get entity @s Pos[1] 1000
execute store result score @s bs.vel.z run data get entity @s Pos[2] 1000

# Scale that unit vector up to the throwing speed
scoreboard players operation @s bs.vel.x *= #900 stoupy_panel.data
scoreboard players operation @s bs.vel.y *= #900 stoupy_panel.data
scoreboard players operation @s bs.vel.z *= #900 stoupy_panel.data
scoreboard players operation @s bs.vel.x /= #1000 stoupy_panel.data
scoreboard players operation @s bs.vel.y /= #1000 stoupy_panel.data
scoreboard players operation @s bs.vel.z /= #1000 stoupy_panel.data

# Back to the thrower's eyes
execute store result storage stoupy_panel:temp tomato_pos.x double 0.001 run scoreboard players get #tomato.x stoupy_panel.data
execute store result storage stoupy_panel:temp tomato_pos.y double 0.001 run scoreboard players get #tomato.y stoupy_panel.data
execute store result storage stoupy_panel:temp tomato_pos.z double 0.001 run scoreboard players get #tomato.z stoupy_panel.data
function stoupy_panel:v1.0.0/tomato/teleport_back with storage stoupy_panel:temp tomato_pos

