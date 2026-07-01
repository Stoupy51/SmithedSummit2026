
#> stewbeet_summit:walls/qol_ecosystem/prev
#
# @executed	positioned 203.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 203.5 101.0 -27.5 & rotated 0 0 ]
#

scoreboard players remove #qol_ecosystem stewbeet_summit.page 1
execute if score #qol_ecosystem stewbeet_summit.page matches ..-1 run scoreboard players set #qol_ecosystem stewbeet_summit.page 0
function stewbeet_summit:walls/qol_ecosystem/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

