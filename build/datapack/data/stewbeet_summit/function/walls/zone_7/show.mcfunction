
#> stewbeet_summit:walls/zone_7/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone_7/next
#			stewbeet_summit:walls/zone_7/prev
#

execute if score #wall7 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone_7/page_0
execute if score #wall7 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone_7/page_1
execute if score #wall7 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone_7/page_2

