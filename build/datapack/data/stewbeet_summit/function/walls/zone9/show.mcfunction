
#> stewbeet_summit:walls/zone9/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone9/next
#			stewbeet_summit:walls/zone9/prev
#

execute if score #wall9 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone9/page0
execute if score #wall9 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone9/page1
execute if score #wall9 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone9/page2
execute if score #wall9 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone9/page3
execute if score #wall9 stewbeet_summit.page matches 4 run function stewbeet_summit:walls/zone9/page4
execute if score #wall9 stewbeet_summit.page matches 5 run function stewbeet_summit:walls/zone9/page5

