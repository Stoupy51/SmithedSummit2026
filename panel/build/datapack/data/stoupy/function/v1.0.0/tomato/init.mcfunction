
#> stoupy:v1.0.0/tomato/init
#
# @executed	anchored eyes & positioned ^ ^ ^0.4
#
# @within	stoupy:v1.0.0/tomato/throw [ anchored eyes & positioned ^ ^ ^0.4 ]
#

tag @s add stoupy.tomato

# Wear the exact item that was thrown, so restyling the tomato needs no change here
loot replace entity @s contents loot stoupy:i/tomato
data modify entity @s billboard set value "vertical"
data modify entity @s brightness set value {sky: 15, block: 15}
data modify entity @s teleport_duration set value 1
data modify entity @s transformation.scale set value [0.55f, 0.55f, 0.55f]

# A tomato thrown at the sky still has to die eventually
scoreboard players set @s stoupy.tomato.life 200

function stoupy:v1.0.0/tomato/velocity

