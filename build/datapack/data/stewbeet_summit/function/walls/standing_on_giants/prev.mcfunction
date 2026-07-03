
#> stewbeet_summit:walls/standing_on_giants/prev
#
# @executed	positioned 194.5 101.0 -19.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 194.5 101.0 -19.5 & rotated 90 0 ]
#

playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
execute if score #standing_on_giants stewbeet_summit.page matches ..0 run return 0
schedule clear stewbeet_summit:walls/standing_on_giants/fade_out_down
schedule clear stewbeet_summit:walls/standing_on_giants/fade_swap_down
schedule clear stewbeet_summit:walls/standing_on_giants/fade_in_down
schedule clear stewbeet_summit:walls/standing_on_giants/fade_out_up
schedule clear stewbeet_summit:walls/standing_on_giants/fade_swap_up
schedule clear stewbeet_summit:walls/standing_on_giants/fade_in_up
scoreboard players remove #standing_on_giants stewbeet_summit.page 1
data merge entity 20180612-2026-2002-2098-202100000005 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/standing_on_giants/pop_settle 2t replace
scoreboard players set #standing_on_giants stewbeet_summit.fc 2
function stewbeet_summit:walls/standing_on_giants/fade_out_up

