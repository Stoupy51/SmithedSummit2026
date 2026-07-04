
#> stewbeet_summit:walls/in_game_manual/show
#
# @within	stewbeet_summit:walls/in_game_manual/fade_swap_down
#			stewbeet_summit:walls/in_game_manual/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#in_game_manual)
execute if score #in_game_manual stewbeet_summit.page matches 0 run function stewbeet_summit:walls/in_game_manual/page_0
execute if score #in_game_manual stewbeet_summit.page matches 1 run function stewbeet_summit:walls/in_game_manual/page_1
execute if score #in_game_manual stewbeet_summit.page matches 2 run function stewbeet_summit:walls/in_game_manual/page_2

