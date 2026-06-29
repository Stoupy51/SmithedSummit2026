
#> stewbeet_summit:walls/zone3/show
#
# @executed	positioned 195.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/zone3/next
#			stewbeet_summit:walls/zone3/prev
#

execute if score #wall3 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone3/page0
execute if score #wall3 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone3/page1
execute if score #wall3 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone3/page2
execute if score #wall3 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone3/page3

