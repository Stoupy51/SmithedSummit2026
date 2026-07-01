
#> stewbeet_summit:walls/zone_7/prev
#
# @executed	positioned 197.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:v0.0.1/load/confirm_load [ positioned 197.5 101.0 -27.5 & rotated 0 0 ]
#

scoreboard players remove #wall7 stewbeet_summit.page 1
execute if score #wall7 stewbeet_summit.page matches ..-1 run scoreboard players set #wall7 stewbeet_summit.page 0
function stewbeet_summit:walls/zone_7/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

