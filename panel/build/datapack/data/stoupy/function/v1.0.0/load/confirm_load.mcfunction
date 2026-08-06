
#> stoupy:v1.0.0/load/confirm_load
#
# @within	stoupy:v1.0.0/load/valid_dependencies
#

# Confirm load
scoreboard players set #stoupy.loaded load.status 1

function stoupy:reef/register_namespace

scoreboard objectives add stoupy.data dummy
scoreboard objectives add stoupy.tomato.life dummy

# Set scoreboard constants for stoupy.data
scoreboard players set #1000 stoupy.data 1000
scoreboard players set #1800 stoupy.data 1800

