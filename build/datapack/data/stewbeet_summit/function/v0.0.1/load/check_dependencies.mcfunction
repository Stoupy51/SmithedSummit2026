
#> stewbeet_summit:v0.0.1/load/check_dependencies
#
# @within	stewbeet_summit:v0.0.1/load/secondary
#

## Check if StewBeet Summit 2026 is loadable (dependencies)
scoreboard players set #dependency_error stewbeet_summit.data 0
execute if score #dependency_error stewbeet_summit.data matches 0 unless score $bs.math.major load.status matches 4.. run scoreboard players set #dependency_error stewbeet_summit.data 1
execute if score #dependency_error stewbeet_summit.data matches 0 if score $bs.math.major load.status matches 4 unless score $bs.math.minor load.status matches 1.. run scoreboard players set #dependency_error stewbeet_summit.data 1

