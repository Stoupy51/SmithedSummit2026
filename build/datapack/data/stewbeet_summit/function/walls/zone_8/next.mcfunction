
#> stewbeet_summit:walls/zone_8/next
#
# @executed	positioned 202.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 202.5 101.0 -24.5 & rotated 180 0 ]
#

scoreboard players add #wall8 stewbeet_summit.page 1
execute if score #wall8 stewbeet_summit.page matches 3.. run scoreboard players set #wall8 stewbeet_summit.page 2
function stewbeet_summit:walls/zone_8/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

