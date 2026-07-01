
#> stewbeet_summit:walls/what_is_stewbeet/show
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/what_is_stewbeet/next
#			stewbeet_summit:walls/what_is_stewbeet/prev
#			stewbeet_summit:walls/reset
#

execute if score #what_is_stewbeet stewbeet_summit.page matches 0 run function stewbeet_summit:walls/what_is_stewbeet/page_0
execute if score #what_is_stewbeet stewbeet_summit.page matches 1 run function stewbeet_summit:walls/what_is_stewbeet/page_1
execute if score #what_is_stewbeet stewbeet_summit.page matches 2 run function stewbeet_summit:walls/what_is_stewbeet/page_2
execute if score #what_is_stewbeet stewbeet_summit.page matches 3 run function stewbeet_summit:walls/what_is_stewbeet/page_3

