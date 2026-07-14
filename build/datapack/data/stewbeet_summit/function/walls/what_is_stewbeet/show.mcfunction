
#> stewbeet_summit:walls/what_is_stewbeet/show
#
# @within	stewbeet_summit:walls/what_is_stewbeet/fade_swap_down
#			stewbeet_summit:walls/what_is_stewbeet/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#what_is_stewbeet)
execute if score #what_is_stewbeet stewbeet_summit.page matches 0 run return run function stewbeet_summit:walls/what_is_stewbeet/page_0
execute if score #what_is_stewbeet stewbeet_summit.page matches 1 run return run function stewbeet_summit:walls/what_is_stewbeet/page_1
execute if score #what_is_stewbeet stewbeet_summit.page matches 2 run return run function stewbeet_summit:walls/what_is_stewbeet/page_2
execute if score #what_is_stewbeet stewbeet_summit.page matches 3 run return run function stewbeet_summit:walls/what_is_stewbeet/page_3

