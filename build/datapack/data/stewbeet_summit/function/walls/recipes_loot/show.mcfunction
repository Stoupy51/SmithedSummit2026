
#> stewbeet_summit:walls/recipes_loot/show
#
# @executed	positioned 191.5 101.0 -22.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/recipes_loot/next
#			stewbeet_summit:walls/recipes_loot/prev
#			stewbeet_summit:walls/reset
#

execute if score #recipes_loot stewbeet_summit.page matches 0 run function stewbeet_summit:walls/recipes_loot/page_0
execute if score #recipes_loot stewbeet_summit.page matches 1 run function stewbeet_summit:walls/recipes_loot/page_1
execute if score #recipes_loot stewbeet_summit.page matches 2 run function stewbeet_summit:walls/recipes_loot/page_2
execute if score #recipes_loot stewbeet_summit.page matches 3 run function stewbeet_summit:walls/recipes_loot/page_3
execute if score #recipes_loot stewbeet_summit.page matches 4 run function stewbeet_summit:walls/recipes_loot/page_4
execute if score #recipes_loot stewbeet_summit.page matches 5 run function stewbeet_summit:walls/recipes_loot/page_5

