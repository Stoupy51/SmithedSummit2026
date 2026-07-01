
#> stewbeet_summit:walls/in_game_manual/next
#
# @executed	positioned 202.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 202.5 101.0 -24.5 & rotated 180 0 ]
#

scoreboard players add #in_game_manual stewbeet_summit.page 1
execute if score #in_game_manual stewbeet_summit.page matches 3.. run scoreboard players set #in_game_manual stewbeet_summit.page 2
function stewbeet_summit:walls/in_game_manual/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

