
#> basic_template:v0.0.1/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #basic_template.major load.status matches 0 if score #basic_template.minor load.status matches 0 if score #basic_template.patch load.status matches 1 run function basic_template:v0.0.1/tick

