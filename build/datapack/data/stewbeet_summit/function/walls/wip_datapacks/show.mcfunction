
#> stewbeet_summit:walls/wip_datapacks/show
#
# @within	stewbeet_summit:walls/wip_datapacks/fade_swap_down
#			stewbeet_summit:walls/wip_datapacks/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#wip_datapacks)
execute if score #wip_datapacks stewbeet_summit.page matches 0 run function stewbeet_summit:walls/wip_datapacks/page_0
execute if score #wip_datapacks stewbeet_summit.page matches 1 run function stewbeet_summit:walls/wip_datapacks/page_1
execute if score #wip_datapacks stewbeet_summit.page matches 2 run function stewbeet_summit:walls/wip_datapacks/page_2
execute if score #wip_datapacks stewbeet_summit.page matches 3 run function stewbeet_summit:walls/wip_datapacks/page_3
execute if score #wip_datapacks stewbeet_summit.page matches 4 run function stewbeet_summit:walls/wip_datapacks/page_4
execute if score #wip_datapacks stewbeet_summit.page matches 5 run function stewbeet_summit:walls/wip_datapacks/page_5

