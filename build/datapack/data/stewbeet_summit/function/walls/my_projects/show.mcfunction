
#> stewbeet_summit:walls/my_projects/show
#
# @within	stewbeet_summit:walls/my_projects/fade_swap_down
#			stewbeet_summit:walls/my_projects/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#my_projects)
execute if score #my_projects stewbeet_summit.page matches 0 run function stewbeet_summit:walls/my_projects/page_0

