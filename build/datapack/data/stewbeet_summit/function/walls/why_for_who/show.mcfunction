
#> stewbeet_summit:walls/why_for_who/show
#
# @within	stewbeet_summit:walls/why_for_who/fade_swap_down
#			stewbeet_summit:walls/why_for_who/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#why_for_who)
execute if score #why_for_who stewbeet_summit.page matches 0 run function stewbeet_summit:walls/why_for_who/page_0
execute if score #why_for_who stewbeet_summit.page matches 1 run function stewbeet_summit:walls/why_for_who/page_1
execute if score #why_for_who stewbeet_summit.page matches 2 run function stewbeet_summit:walls/why_for_who/page_2
execute if score #why_for_who stewbeet_summit.page matches 3 run function stewbeet_summit:walls/why_for_who/page_3

