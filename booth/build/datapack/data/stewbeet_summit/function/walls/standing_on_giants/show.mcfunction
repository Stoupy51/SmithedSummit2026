
#> stewbeet_summit:walls/standing_on_giants/show
#
# @within	stewbeet_summit:walls/standing_on_giants/fade_swap_down
#			stewbeet_summit:walls/standing_on_giants/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#standing_on_giants)
execute if score #standing_on_giants stewbeet_summit.page matches 0 run return run function stewbeet_summit:walls/standing_on_giants/page_0
execute if score #standing_on_giants stewbeet_summit.page matches 1 run return run function stewbeet_summit:walls/standing_on_giants/page_1
execute if score #standing_on_giants stewbeet_summit.page matches 2 run return run function stewbeet_summit:walls/standing_on_giants/page_2
execute if score #standing_on_giants stewbeet_summit.page matches 3 run return run function stewbeet_summit:walls/standing_on_giants/page_3
execute if score #standing_on_giants stewbeet_summit.page matches 4 run return run function stewbeet_summit:walls/standing_on_giants/page_4
execute if score #standing_on_giants stewbeet_summit.page matches 5 run return run function stewbeet_summit:walls/standing_on_giants/page_5
execute if score #standing_on_giants stewbeet_summit.page matches 6 run return run function stewbeet_summit:walls/standing_on_giants/page_6

