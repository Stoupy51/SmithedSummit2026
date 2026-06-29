
#> stewbeet_summit:walls/zone8/show
#
# @executed	positioned 200.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/zone8/next
#			stewbeet_summit:walls/zone8/prev
#

execute if score #wall8 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone8/page0
execute if score #wall8 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone8/page1
execute if score #wall8 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone8/page2

