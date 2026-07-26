
#> stoupy_panel:v1.0.0/load/resolve
#
# @within	#stoupy_panel:resolve
#

# If correct version, load the datapack
execute if score #stoupy_panel.major load.status matches 1 if score #stoupy_panel.minor load.status matches 0 if score #stoupy_panel.patch load.status matches 0 run function stoupy_panel:v1.0.0/load/main

