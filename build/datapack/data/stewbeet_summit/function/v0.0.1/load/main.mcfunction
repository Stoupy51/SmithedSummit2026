
#> stewbeet_summit:v0.0.1/load/main
#
# @within	stewbeet_summit:v0.0.1/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #stewbeet_summit.loaded load.status matches 1 run function stewbeet_summit:v0.0.1/load/secondary

