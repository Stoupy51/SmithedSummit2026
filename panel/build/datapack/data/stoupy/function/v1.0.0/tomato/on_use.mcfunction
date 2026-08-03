
#> stoupy:v1.0.0/tomato/on_use
#
# @executed	as the player & at current position
#
# @within	advancement stoupy:tomato/use
#

# One throw per press, not one per tick spent holding the button
execute if entity @s[tag=stoupy.tomato.used] run return 0
tag @s add stoupy.tomato.used

function stoupy:v1.0.0/tomato/throw

