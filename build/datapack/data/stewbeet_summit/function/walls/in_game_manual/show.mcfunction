
#> stewbeet_summit:walls/in_game_manual/show
#
# @executed	positioned 202.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/in_game_manual/next
#			stewbeet_summit:walls/in_game_manual/prev
#			stewbeet_summit:walls/reset
#

execute if score #in_game_manual stewbeet_summit.page matches 0 run function stewbeet_summit:walls/in_game_manual/page_0
execute if score #in_game_manual stewbeet_summit.page matches 1 run function stewbeet_summit:walls/in_game_manual/page_1
execute if score #in_game_manual stewbeet_summit.page matches 2 run function stewbeet_summit:walls/in_game_manual/page_2

