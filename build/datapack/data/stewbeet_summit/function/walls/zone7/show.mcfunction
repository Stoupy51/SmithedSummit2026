
#> stewbeet_summit:walls/zone7/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone7/next
#			stewbeet_summit:walls/zone7/prev
#

execute if score #wall7 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone7/page0
execute if score #wall7 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone7/page1
execute if score #wall7 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone7/page2
execute if score #wall7 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone7/page3

