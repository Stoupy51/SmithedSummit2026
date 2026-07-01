
#> stewbeet_summit:walls/standing_on_giants/next
#
# @executed	positioned 194.5 101.0 -19.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 194.5 101.0 -19.5 & rotated 90 0 ]
#

scoreboard players add #standing_on_giants stewbeet_summit.page 1
execute if score #standing_on_giants stewbeet_summit.page matches 7.. run scoreboard players set #standing_on_giants stewbeet_summit.page 6
function stewbeet_summit:walls/standing_on_giants/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

