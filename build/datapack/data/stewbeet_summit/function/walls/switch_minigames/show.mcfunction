
#> stewbeet_summit:walls/switch_minigames/show
#
# @within	stewbeet_summit:walls/switch_minigames/fade_swap_down
#			stewbeet_summit:walls/switch_minigames/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#switch_minigames)
execute if score #switch_minigames stewbeet_summit.page matches 0 run function stewbeet_summit:walls/switch_minigames/page_0
execute if score #switch_minigames stewbeet_summit.page matches 1 run function stewbeet_summit:walls/switch_minigames/page_1
execute if score #switch_minigames stewbeet_summit.page matches 2 run function stewbeet_summit:walls/switch_minigames/page_2

