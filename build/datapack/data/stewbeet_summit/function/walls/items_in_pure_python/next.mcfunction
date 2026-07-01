
#> stewbeet_summit:walls/items_in_pure_python/next
#
# @executed	positioned 196.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 196.5 101.0 -11.5 & rotated 180 0 ]
#

scoreboard players add #items_in_pure_python stewbeet_summit.page 1
execute if score #items_in_pure_python stewbeet_summit.page matches 5.. run scoreboard players set #items_in_pure_python stewbeet_summit.page 4
function stewbeet_summit:walls/items_in_pure_python/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

