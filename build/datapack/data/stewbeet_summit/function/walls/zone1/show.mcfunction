
#> stewbeet_summit:walls/zone1/show
#
# @executed	positioned 204.5 101.0 -22.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/zone1/next
#			stewbeet_summit:walls/zone1/prev
#

execute if score #wall1 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone1/page0
execute if score #wall1 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone1/page1
execute if score #wall1 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone1/page2
execute if score #wall1 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone1/page3

