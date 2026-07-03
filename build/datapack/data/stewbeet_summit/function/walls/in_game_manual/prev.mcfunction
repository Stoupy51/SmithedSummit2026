
#> stewbeet_summit:walls/in_game_manual/prev
#
# @executed	positioned 202.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 202.5 101.0 -24.5 & rotated 180 0 ]
#

scoreboard players remove #in_game_manual stewbeet_summit.page 1
execute if score #in_game_manual stewbeet_summit.page matches ..-1 run scoreboard players set #in_game_manual stewbeet_summit.page 0
function stewbeet_summit:walls/in_game_manual/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
data merge entity 20180612-2026-2002-2098-202100000008 {interpolation_duration:0,start_interpolation:0,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/in_game_manual/pop_settle 2t replace

