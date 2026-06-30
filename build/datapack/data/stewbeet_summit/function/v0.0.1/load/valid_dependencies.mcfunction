
#> stewbeet_summit:v0.0.1/load/valid_dependencies
#
# @within	stewbeet_summit:v0.0.1/load/secondary
#			stewbeet_summit:v0.0.1/load/valid_dependencies 1t replace [ scheduled ]
#

# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run return run schedule function stewbeet_summit:v0.0.1/load/valid_dependencies 1t replace
execute store result score #game_version stewbeet_summit.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error stewbeet_summit.data 0
execute unless score #game_version stewbeet_summit.data matches 4903.. run scoreboard players set #mcload_error stewbeet_summit.data 1

# Decode errors
execute if score #mcload_error stewbeet_summit.data matches 1 run tellraw @a {"text":"StewBeet Summit 2026 Error: This version is made for Minecraft 26.2+.","color":"red"}
execute if score #dependency_error stewbeet_summit.data matches 1 run tellraw @a {"text":"StewBeet Summit 2026 Error: Libraries are missing\nplease download the right StewBeet Summit 2026 datapack\nor download each of these libraries one by one:","color":"red"}
execute if score #dependency_error stewbeet_summit.data matches 1 unless score $bs.math.major load.status matches 4.. run tellraw @a {"text":"- [Bookshelf Math (v4.1.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/mcbookshelf/bookshelf/releases"}}
execute if score #dependency_error stewbeet_summit.data matches 1 if score $bs.math.major load.status matches 4 unless score $bs.math.minor load.status matches 1.. run tellraw @a {"text":"- [Bookshelf Math (v4.1.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/mcbookshelf/bookshelf/releases"}}

# Load StewBeet Summit 2026
execute if score #game_version stewbeet_summit.data matches 1.. if score #mcload_error stewbeet_summit.data matches 0 if score #dependency_error stewbeet_summit.data matches 0 run function stewbeet_summit:v0.0.1/load/confirm_load

