
#> stewbeet_summit:walls/zone5/next
#
# @executed	positioned 194.5 101.0 -19.5 & rotated 90 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 194.5 101.0 -19.5 & rotated 90 0 ]
#

scoreboard players add #wall5 stewbeet_summit.page 1
execute if score #wall5 stewbeet_summit.page matches 3.. run scoreboard players set #wall5 stewbeet_summit.page 2
function stewbeet_summit:walls/zone5/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

