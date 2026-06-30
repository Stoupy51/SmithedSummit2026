
#> stewbeet_summit:walls/zone6/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone6/next
#			stewbeet_summit:walls/zone6/prev
#

execute if score #wall6 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone6/page0
execute if score #wall6 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone6/page1
execute if score #wall6 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone6/page2

