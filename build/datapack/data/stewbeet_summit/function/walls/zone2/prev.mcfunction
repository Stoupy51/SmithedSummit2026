
#> stewbeet_summit:walls/zone2/prev
#
# @executed	positioned 201.5 101.0 -19.5 & rotated 180 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 201.5 101.0 -19.5 & rotated 180 0 ]
#

scoreboard players remove #wall2 stewbeet_summit.page 1
execute if score #wall2 stewbeet_summit.page matches ..-1 run scoreboard players set #wall2 stewbeet_summit.page 0
function stewbeet_summit:walls/zone2/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

