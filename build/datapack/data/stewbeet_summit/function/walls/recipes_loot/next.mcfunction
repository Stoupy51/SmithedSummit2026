
#> stewbeet_summit:walls/recipes_loot/next
#
# @executed	positioned 191.5 101.0 -22.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 191.5 101.0 -22.5 & rotated -90 0 ]
#

scoreboard players add #recipes_loot stewbeet_summit.page 1
execute if score #recipes_loot stewbeet_summit.page matches 6.. run scoreboard players set #recipes_loot stewbeet_summit.page 5
function stewbeet_summit:walls/recipes_loot/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

