
#> stoupy:v1.0.0/load/valid_dependencies
#
# @within	stoupy:v1.0.0/load/secondary
#			stoupy:v1.0.0/load/valid_dependencies 1t replace [ scheduled ]
#

# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run return run schedule function stoupy:v1.0.0/load/valid_dependencies 1t replace
execute store result score #game_version stoupy.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error stoupy.data 0
execute unless score #game_version stoupy.data matches 4903.. run scoreboard players set #mcload_error stoupy.data 1

# Decode errors
execute if score #mcload_error stoupy.data matches 1 run tellraw @a {"text":"Boost Your Productivity Error: This version is made for Minecraft 26.2+.","color":"red"}
execute if score #dependency_error stoupy.data matches 1 run tellraw @a {"text":"Boost Your Productivity Error: Libraries are missing\nplease download the right Boost Your Productivity datapack\nor download each of these libraries one by one:","color":"red"}
execute if score #dependency_error stoupy.data matches 1 unless score $bs.move.major load.status matches 4.. run tellraw @a {"text":"- [Bookshelf Move (v4.1.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/mcbookshelf/bookshelf/releases"}}
execute if score #dependency_error stoupy.data matches 1 if score $bs.move.major load.status matches 4 unless score $bs.move.minor load.status matches 1.. run tellraw @a {"text":"- [Bookshelf Move (v4.1.0+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/mcbookshelf/bookshelf/releases"}}

# Load Boost Your Productivity
execute if score #game_version stoupy.data matches 1.. if score #mcload_error stoupy.data matches 0 if score #dependency_error stoupy.data matches 0 run function stoupy:v1.0.0/load/confirm_load

