
#> stoupy_panel:v1.0.0/tomato/on_use
#
# @executed	as the player & at current position
#
# @within	advancement stoupy_panel:tomato/use
#

# One throw per press, not one per tick spent holding the button
execute if entity @s[tag=stoupy_panel.tomato.used] run return 0
tag @s add stoupy_panel.tomato.used

function stoupy_panel:v1.0.0/tomato/throw

