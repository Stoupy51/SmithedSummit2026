
#> stewbeet_summit:walls/zone3/next
#
# @executed	positioned 195.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 195.5 101.0 -11.5 & rotated 180 0 ]
#

scoreboard players add #wall3 stewbeet_summit.page 1
execute if score #wall3 stewbeet_summit.page matches 4.. run scoreboard players set #wall3 stewbeet_summit.page 4
function stewbeet_summit:walls/zone3/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

