
#> stoupy_panel:v1.0.0/load/check_dependencies
#
# @within	stoupy_panel:v1.0.0/load/secondary
#

## Check if Boost Your Productivity is loadable (dependencies)
scoreboard players set #dependency_error stoupy_panel.data 0
execute if score #dependency_error stoupy_panel.data matches 0 unless score $bs.move.major load.status matches 4.. run scoreboard players set #dependency_error stoupy_panel.data 1
execute if score #dependency_error stoupy_panel.data matches 0 if score $bs.move.major load.status matches 4 unless score $bs.move.minor load.status matches 1.. run scoreboard players set #dependency_error stoupy_panel.data 1

