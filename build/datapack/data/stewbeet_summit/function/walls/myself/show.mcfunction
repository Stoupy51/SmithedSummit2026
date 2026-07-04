
#> stewbeet_summit:walls/myself/show
#
# @within	stewbeet_summit:walls/myself/fade_swap_down
#			stewbeet_summit:walls/myself/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#myself)
execute if score #myself stewbeet_summit.page matches 0 run function stewbeet_summit:walls/myself/page_0
execute if score #myself stewbeet_summit.page matches 1 run function stewbeet_summit:walls/myself/page_1
execute if score #myself stewbeet_summit.page matches 2 run function stewbeet_summit:walls/myself/page_2

