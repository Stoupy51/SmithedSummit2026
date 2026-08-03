
#> stoupy:v1.0.0/unload
#
# @within	#stoupy:unload
#

# Clear custom items
clear @a *[custom_data~{"stoupy":{}}]

# Remove scoreboard objectives
scoreboard objectives remove load.status
scoreboard objectives remove stoupy.data
scoreboard objectives remove stoupy.tomato.life

# Clear storages
data remove storage stoupy:items all
data remove storage stoupy:reef register

