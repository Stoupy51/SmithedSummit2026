
#> stewbeet_summit:walls/start_in_3_commands/show
#
# @within	stewbeet_summit:walls/start_in_3_commands/fade_swap_down
#			stewbeet_summit:walls/start_in_3_commands/fade_swap_up
#			stewbeet_summit:walls/reset
#

execute if score #start_in_3_commands stewbeet_summit.page matches 0 run function stewbeet_summit:walls/start_in_3_commands/page_0
execute if score #start_in_3_commands stewbeet_summit.page matches 1 run function stewbeet_summit:walls/start_in_3_commands/page_1
execute if score #start_in_3_commands stewbeet_summit.page matches 2 run function stewbeet_summit:walls/start_in_3_commands/page_2
execute if score #start_in_3_commands stewbeet_summit.page matches 3 run function stewbeet_summit:walls/start_in_3_commands/page_3

