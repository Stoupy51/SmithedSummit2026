
#> stewbeet_summit:walls/generate_material_sets/show
#
# @executed	positioned 197.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/generate_material_sets/next
#			stewbeet_summit:walls/generate_material_sets/prev
#			stewbeet_summit:walls/reset
#

execute if score #generate_material_sets stewbeet_summit.page matches 0 run function stewbeet_summit:walls/generate_material_sets/page_0
execute if score #generate_material_sets stewbeet_summit.page matches 1 run function stewbeet_summit:walls/generate_material_sets/page_1
execute if score #generate_material_sets stewbeet_summit.page matches 2 run function stewbeet_summit:walls/generate_material_sets/page_2

