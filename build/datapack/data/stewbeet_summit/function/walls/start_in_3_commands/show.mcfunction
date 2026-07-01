
#> stewbeet_summit:walls/start_in_3_commands/show
#
# @executed	positioned 201.5 101.0 -19.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/start_in_3_commands/next
#			stewbeet_summit:walls/start_in_3_commands/prev
#			stewbeet_summit:walls/reset
#

execute if score #start_in_3_commands stewbeet_summit.page matches 0 run function stewbeet_summit:walls/start_in_3_commands/page_0
execute if score #start_in_3_commands stewbeet_summit.page matches 1 run function stewbeet_summit:walls/start_in_3_commands/page_1
execute if score #start_in_3_commands stewbeet_summit.page matches 2 run function stewbeet_summit:walls/start_in_3_commands/page_2
execute if score #start_in_3_commands stewbeet_summit.page matches 3 run function stewbeet_summit:walls/start_in_3_commands/page_3

