
#> stewbeet_summit:walls/custom_blocks_made_easy/show
#
# @within	stewbeet_summit:walls/custom_blocks_made_easy/fade_swap_down
#			stewbeet_summit:walls/custom_blocks_made_easy/fade_swap_up
#			stewbeet_summit:walls/reset
#

execute if score #custom_blocks_made_easy stewbeet_summit.page matches 0 run function stewbeet_summit:walls/custom_blocks_made_easy/page_0
execute if score #custom_blocks_made_easy stewbeet_summit.page matches 1 run function stewbeet_summit:walls/custom_blocks_made_easy/page_1
execute if score #custom_blocks_made_easy stewbeet_summit.page matches 2 run function stewbeet_summit:walls/custom_blocks_made_easy/page_2
execute if score #custom_blocks_made_easy stewbeet_summit.page matches 3 run function stewbeet_summit:walls/custom_blocks_made_easy/page_3
execute if score #custom_blocks_made_easy stewbeet_summit.page matches 4 run function stewbeet_summit:walls/custom_blocks_made_easy/page_4
execute if score #custom_blocks_made_easy stewbeet_summit.page matches 5 run function stewbeet_summit:walls/custom_blocks_made_easy/page_5

