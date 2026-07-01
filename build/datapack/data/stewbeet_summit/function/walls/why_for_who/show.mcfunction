
#> stewbeet_summit:walls/why_for_who/show
#
# @executed	positioned 204.5 101.0 -22.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/why_for_who/next
#			stewbeet_summit:walls/why_for_who/prev
#			stewbeet_summit:walls/reset
#

execute if score #why_for_who stewbeet_summit.page matches 0 run function stewbeet_summit:walls/why_for_who/page_0
execute if score #why_for_who stewbeet_summit.page matches 1 run function stewbeet_summit:walls/why_for_who/page_1
execute if score #why_for_who stewbeet_summit.page matches 2 run function stewbeet_summit:walls/why_for_who/page_2
execute if score #why_for_who stewbeet_summit.page matches 3 run function stewbeet_summit:walls/why_for_who/page_3

