
#> stewbeet_summit:walls/standing_on_giants/show
#
# @executed	positioned 194.5 101.0 -19.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/standing_on_giants/next
#			stewbeet_summit:walls/standing_on_giants/prev
#			stewbeet_summit:walls/reset
#

execute if score #standing_on_giants stewbeet_summit.page matches 0 run function stewbeet_summit:walls/standing_on_giants/page_0
execute if score #standing_on_giants stewbeet_summit.page matches 1 run function stewbeet_summit:walls/standing_on_giants/page_1
execute if score #standing_on_giants stewbeet_summit.page matches 2 run function stewbeet_summit:walls/standing_on_giants/page_2
execute if score #standing_on_giants stewbeet_summit.page matches 3 run function stewbeet_summit:walls/standing_on_giants/page_3
execute if score #standing_on_giants stewbeet_summit.page matches 4 run function stewbeet_summit:walls/standing_on_giants/page_4
execute if score #standing_on_giants stewbeet_summit.page matches 5 run function stewbeet_summit:walls/standing_on_giants/page_5
execute if score #standing_on_giants stewbeet_summit.page matches 6 run function stewbeet_summit:walls/standing_on_giants/page_6

