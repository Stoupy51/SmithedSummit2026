
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
data merge entity 20180612-2026-2002-2098-202100000002 {interpolation_duration:0,start_interpolation:0,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/start_in_3_commands/pop_settle 2t replace

