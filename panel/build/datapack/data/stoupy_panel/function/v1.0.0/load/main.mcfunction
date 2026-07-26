
#> stoupy_panel:v1.0.0/load/main
#
# @within	stoupy_panel:v1.0.0/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #stoupy_panel.loaded load.status matches 1 run function stoupy_panel:v1.0.0/load/secondary

