
#> stewbeet_summit:walls/generate_material_sets/next
#
# @executed	positioned 197.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 197.5 101.0 -27.5 & rotated 0 0 ]
#

scoreboard players add #generate_material_sets stewbeet_summit.page 1
execute if score #generate_material_sets stewbeet_summit.page matches 3.. run scoreboard players set #generate_material_sets stewbeet_summit.page 2
function stewbeet_summit:walls/generate_material_sets/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

