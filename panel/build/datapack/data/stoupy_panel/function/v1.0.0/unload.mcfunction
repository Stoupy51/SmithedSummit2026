
#> stoupy_panel:v1.0.0/unload
#
# @within	#stoupy_panel:unload
#

# Clear custom items
clear @a *[custom_data~{"stoupy_panel":{}}]

# Remove scoreboard objectives
scoreboard objectives remove load.status
scoreboard objectives remove stoupy_panel.data
scoreboard objectives remove stoupy_panel.tomato.life

# Clear storages
data remove storage stoupy_panel:items all
data remove storage stoupy_panel:reef register

