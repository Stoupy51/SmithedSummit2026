
#> stoupy_panel:v1.0.0/load/confirm_load
#
# @within	stoupy_panel:v1.0.0/load/valid_dependencies
#

# Confirm load
scoreboard players set #stoupy_panel.loaded load.status 1

function stoupy_panel:reef/register_namespace

scoreboard objectives add stoupy_panel.data dummy
scoreboard objectives add stoupy_panel.tomato.life dummy

# Set scoreboard constants for stoupy_panel.data
scoreboard players set #900 stoupy_panel.data 900
scoreboard players set #1000 stoupy_panel.data 1000

