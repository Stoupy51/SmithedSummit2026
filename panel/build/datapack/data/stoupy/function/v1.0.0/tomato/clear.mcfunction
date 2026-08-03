
#> stoupy:v1.0.0/tomato/clear
#
# @within	stoupy:tomato/clear
#

execute as @e[type=item_display, tag=stoupy.tomato] at @s run function stoupy:v1.0.0/tomato/splat
clear @a *[minecraft:custom_data~{stoupy: {tomato: true}}]
tellraw @a {"text": "That is enough tomatoes, thank you.", "color": "gray", "italic": true}

