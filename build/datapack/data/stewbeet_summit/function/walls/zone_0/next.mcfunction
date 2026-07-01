
#> stewbeet_summit:walls/zone_0/next
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 211.5 101.0 -18.5 & rotated 90 0 ]
#

scoreboard players add #wall0 stewbeet_summit.page 1
execute if score #wall0 stewbeet_summit.page matches 4.. run scoreboard players set #wall0 stewbeet_summit.page 3
function stewbeet_summit:walls/zone_0/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

