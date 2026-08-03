
#> stoupy:v1.0.0/load/resolve
#
# @within	#stoupy:resolve
#

# If correct version, load the datapack
execute if score #stoupy.major load.status matches 1 if score #stoupy.minor load.status matches 0 if score #stoupy.patch load.status matches 0 run function stoupy:v1.0.0/load/main

