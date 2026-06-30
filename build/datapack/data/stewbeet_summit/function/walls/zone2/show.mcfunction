
#> stewbeet_summit:walls/zone2/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone2/next
#			stewbeet_summit:walls/zone2/prev
#

execute if score #wall2 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone2/page0
execute if score #wall2 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone2/page1
execute if score #wall2 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone2/page2
execute if score #wall2 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone2/page3

