
#> stoupy_panel:v1.0.0/tomato/clear
#
# @within	stoupy_panel:tomato/clear
#

execute as @e[type=item_display, tag=stoupy_panel.tomato] at @s run function stoupy_panel:v1.0.0/tomato/splat
clear @a *[minecraft:custom_data~{stoupy_panel: {tomato: true}}]
tellraw @a {"translate": "stoupy_panel.that_is_enough_tomatoes_thank_you", "color": "gray", "italic": true}

