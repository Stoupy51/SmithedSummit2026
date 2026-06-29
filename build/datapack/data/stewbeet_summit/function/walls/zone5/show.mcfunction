
#> stewbeet_summit:walls/zone5/show
#
# @executed	positioned 194.5 101.0 -19.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/zone5/next
#			stewbeet_summit:walls/zone5/prev
#

execute if score #wall5 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone5/page0
execute if score #wall5 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone5/page1
execute if score #wall5 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone5/page2

