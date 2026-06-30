
#> stewbeet_summit:walls/zone5/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone5/next
#			stewbeet_summit:walls/zone5/prev
#

execute if score #wall5 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone5/page0
execute if score #wall5 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone5/page1
execute if score #wall5 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone5/page2
execute if score #wall5 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone5/page3
execute if score #wall5 stewbeet_summit.page matches 4 run function stewbeet_summit:walls/zone5/page4
execute if score #wall5 stewbeet_summit.page matches 5 run function stewbeet_summit:walls/zone5/page5
execute if score #wall5 stewbeet_summit.page matches 6 run function stewbeet_summit:walls/zone5/page6

