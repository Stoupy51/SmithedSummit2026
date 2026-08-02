
#> stoupy_panel:v1.0.0/load/valid_dependencies
#
# @within	stoupy_panel:v1.0.0/load/secondary
#			stoupy_panel:v1.0.0/load/valid_dependencies 1t replace [ scheduled ]
#

# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run return run schedule function stoupy_panel:v1.0.0/load/valid_dependencies 1t replace
execute store result score #game_version stoupy_panel.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error stoupy_panel.data 0
execute unless score #game_version stoupy_panel.data matches 4903.. run scoreboard players set #mcload_error stoupy_panel.data 1

# Decode errors
execute if score #mcload_error stoupy_panel.data matches 1 run tellraw @a {"translate":"stoupy_panel.boost_your_productivity_error_this_version_is_made_for_minecraft","color":"red"}
execute if score #dependency_error stoupy_panel.data matches 1 run tellraw @a {"translate":"stoupy_panel.boost_your_productivity_error_libraries_are_missingplease_downlo","color":"red"}
execute if score #dependency_error stoupy_panel.data matches 1 unless score $bs.move.major load.status matches 4.. run tellraw @a [{"text":"- ","color":"gold","click_event":{"action":"open_url","url":"https://github.com/mcbookshelf/bookshelf/releases"}}, {"translate":"stoupy_panel.bookshelf_move_v4_1_0"}]
execute if score #dependency_error stoupy_panel.data matches 1 if score $bs.move.major load.status matches 4 unless score $bs.move.minor load.status matches 1.. run tellraw @a [{"text":"- ","color":"gold","click_event":{"action":"open_url","url":"https://github.com/mcbookshelf/bookshelf/releases"}}, {"translate":"stoupy_panel.bookshelf_move_v4_1_0"}]

# Load Boost Your Productivity
execute if score #game_version stoupy_panel.data matches 1.. if score #mcload_error stoupy_panel.data matches 0 if score #dependency_error stoupy_panel.data matches 0 run function stoupy_panel:v1.0.0/load/confirm_load

