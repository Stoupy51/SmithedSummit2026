
#> stewbeet_summit:walls/zone1/prev
#
# @executed	positioned 204.5 101.0 -22.5 & rotated 0 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 204.5 101.0 -22.5 & rotated 0 0 ]
#

scoreboard players remove #wall1 stewbeet_summit.page 1
execute if score #wall1 stewbeet_summit.page matches ..-1 run scoreboard players set #wall1 stewbeet_summit.page 0
function stewbeet_summit:walls/zone1/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

