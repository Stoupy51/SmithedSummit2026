
#> stewbeet_summit:walls/items_in_pure_python/show
#
# @within	stewbeet_summit:walls/items_in_pure_python/fade_swap_down
#			stewbeet_summit:walls/items_in_pure_python/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#items_in_pure_python)
execute if score #items_in_pure_python stewbeet_summit.page matches 0 run return run function stewbeet_summit:walls/items_in_pure_python/page_0
execute if score #items_in_pure_python stewbeet_summit.page matches 1 run return run function stewbeet_summit:walls/items_in_pure_python/page_1
execute if score #items_in_pure_python stewbeet_summit.page matches 2 run return run function stewbeet_summit:walls/items_in_pure_python/page_2
execute if score #items_in_pure_python stewbeet_summit.page matches 3 run return run function stewbeet_summit:walls/items_in_pure_python/page_3
execute if score #items_in_pure_python stewbeet_summit.page matches 4 run return run function stewbeet_summit:walls/items_in_pure_python/page_4

