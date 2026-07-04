
#> stewbeet_summit:v1.0.0/load/resolve
#
# @within	#stewbeet_summit:resolve
#

# If correct version, load the datapack
execute if score #stewbeet_summit.major load.status matches 1 if score #stewbeet_summit.minor load.status matches 0 if score #stewbeet_summit.patch load.status matches 0 run function stewbeet_summit:v1.0.0/load/main

