
#> stewbeet_summit:walls/material_sets/prev
#
# @executed	positioned 197.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 197.5 101.0 -27.5 & rotated 0 0 ]
#

playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
execute if score #material_sets stewbeet_summit.page matches ..0 run return 0
schedule clear stewbeet_summit:walls/material_sets/fade_out_down
schedule clear stewbeet_summit:walls/material_sets/fade_swap_down
schedule clear stewbeet_summit:walls/material_sets/fade_in_down
schedule clear stewbeet_summit:walls/material_sets/fade_out_up
schedule clear stewbeet_summit:walls/material_sets/fade_swap_up
schedule clear stewbeet_summit:walls/material_sets/fade_in_up
scoreboard players remove #material_sets stewbeet_summit.page 1
data merge entity 20180612-2026-2002-2098-202100000007 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/material_sets/pop_settle 2t replace
scoreboard players set #material_sets stewbeet_summit.fc 2
function stewbeet_summit:walls/material_sets/fade_out_up

