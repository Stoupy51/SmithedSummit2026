
#> stewbeet_summit:walls/zone_4/next
#
# @executed	positioned 191.5 101.0 -16.5 & rotated -90 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 191.5 101.0 -16.5 & rotated -90 0 ]
#

scoreboard players add #wall4 stewbeet_summit.page 1
execute if score #wall4 stewbeet_summit.page matches 6.. run scoreboard players set #wall4 stewbeet_summit.page 5
function stewbeet_summit:walls/zone_4/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

