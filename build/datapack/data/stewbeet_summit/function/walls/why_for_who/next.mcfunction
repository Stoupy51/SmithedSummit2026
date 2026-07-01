
#> stewbeet_summit:walls/why_for_who/next
#
# @executed	positioned 204.5 101.0 -22.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 204.5 101.0 -22.5 & rotated 0 0 ]
#

scoreboard players add #why_for_who stewbeet_summit.page 1
execute if score #why_for_who stewbeet_summit.page matches 4.. run scoreboard players set #why_for_who stewbeet_summit.page 3
function stewbeet_summit:walls/why_for_who/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

