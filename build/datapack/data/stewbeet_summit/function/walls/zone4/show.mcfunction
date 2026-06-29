
#> stewbeet_summit:walls/zone4/show
#
# @executed	positioned 191.5 101.0 -16.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/zone4/next
#			stewbeet_summit:walls/zone4/prev
#

execute if score #wall4 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone4/page0
execute if score #wall4 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone4/page1
execute if score #wall4 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone4/page2
execute if score #wall4 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone4/page3

