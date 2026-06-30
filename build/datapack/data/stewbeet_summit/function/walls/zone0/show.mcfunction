
#> stewbeet_summit:walls/zone0/show
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load
#			stewbeet_summit:walls/zone0/next
#			stewbeet_summit:walls/zone0/prev
#

execute if score #wall0 stewbeet_summit.page matches 0 run function stewbeet_summit:walls/zone0/page0
execute if score #wall0 stewbeet_summit.page matches 1 run function stewbeet_summit:walls/zone0/page1
execute if score #wall0 stewbeet_summit.page matches 2 run function stewbeet_summit:walls/zone0/page2
execute if score #wall0 stewbeet_summit.page matches 3 run function stewbeet_summit:walls/zone0/page3

