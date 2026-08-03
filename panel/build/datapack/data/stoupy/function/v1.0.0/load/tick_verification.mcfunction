
#> stoupy:v1.0.0/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #stoupy.major load.status matches 1 if score #stoupy.minor load.status matches 0 if score #stoupy.patch load.status matches 0 run function stoupy:v1.0.0/tick

