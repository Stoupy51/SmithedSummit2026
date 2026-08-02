
#> stoupy_panel:v1.0.0/tomato/disable
#
# @within	stoupy_panel:tomato/disable
#

scoreboard players set #tomato.enabled stoupy_panel.data 0
function stoupy_panel:v1.0.0/tomato/clear
tellraw @a {"translate": "stoupy_panel.that_is_enough_tomatoes_thank_you", "color": "gray", "italic": true}

