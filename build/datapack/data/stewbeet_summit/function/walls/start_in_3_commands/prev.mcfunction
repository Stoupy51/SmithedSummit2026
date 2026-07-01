
#> stewbeet_summit:walls/start_in_3_commands/prev
#
# @executed	positioned 201.5 101.0 -19.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 201.5 101.0 -19.5 & rotated 180 0 ]
#

scoreboard players remove #start_in_3_commands stewbeet_summit.page 1
execute if score #start_in_3_commands stewbeet_summit.page matches ..-1 run scoreboard players set #start_in_3_commands stewbeet_summit.page 0
function stewbeet_summit:walls/start_in_3_commands/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

