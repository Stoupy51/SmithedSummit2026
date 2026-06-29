
#> stewbeet_summit:walls/zone8/prev
#
# @executed	positioned 200.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 200.5 101.0 -24.5 & rotated 180 0 ]
#

scoreboard players remove #wall8 stewbeet_summit.page 1
execute if score #wall8 stewbeet_summit.page matches ..-1 run scoreboard players set #wall8 stewbeet_summit.page 0
function stewbeet_summit:walls/zone8/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

