
#> stewbeet_summit:walls/qol_ecosystem/show
#
# @within	stewbeet_summit:walls/qol_ecosystem/fade_swap_down
#			stewbeet_summit:walls/qol_ecosystem/fade_swap_up
#			stewbeet_summit:walls/reset
#

execute if score #qol_ecosystem stewbeet_summit.page matches 0 run function stewbeet_summit:walls/qol_ecosystem/page_0
execute if score #qol_ecosystem stewbeet_summit.page matches 1 run function stewbeet_summit:walls/qol_ecosystem/page_1
execute if score #qol_ecosystem stewbeet_summit.page matches 2 run function stewbeet_summit:walls/qol_ecosystem/page_2
execute if score #qol_ecosystem stewbeet_summit.page matches 3 run function stewbeet_summit:walls/qol_ecosystem/page_3
execute if score #qol_ecosystem stewbeet_summit.page matches 4 run function stewbeet_summit:walls/qol_ecosystem/page_4
execute if score #qol_ecosystem stewbeet_summit.page matches 5 run function stewbeet_summit:walls/qol_ecosystem/page_5

