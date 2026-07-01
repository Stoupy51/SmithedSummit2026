
#> stewbeet_summit:walls/items_in_pure_python/show
#
# @executed	positioned 196.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/items_in_pure_python/next
#			stewbeet_summit:walls/items_in_pure_python/prev
#			stewbeet_summit:walls/reset
#

execute if score #items_in_pure_python stewbeet_summit.page matches 0 run function stewbeet_summit:walls/items_in_pure_python/page_0
execute if score #items_in_pure_python stewbeet_summit.page matches 1 run function stewbeet_summit:walls/items_in_pure_python/page_1
execute if score #items_in_pure_python stewbeet_summit.page matches 2 run function stewbeet_summit:walls/items_in_pure_python/page_2
execute if score #items_in_pure_python stewbeet_summit.page matches 3 run function stewbeet_summit:walls/items_in_pure_python/page_3
execute if score #items_in_pure_python stewbeet_summit.page matches 4 run function stewbeet_summit:walls/items_in_pure_python/page_4

