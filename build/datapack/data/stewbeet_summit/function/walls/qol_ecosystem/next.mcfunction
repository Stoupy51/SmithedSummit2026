
#> stewbeet_summit:walls/qol_ecosystem/next
#
# @executed	positioned 203.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 203.5 101.0 -27.5 & rotated 0 0 ]
#

playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
execute if score #qol_ecosystem stewbeet_summit.page matches 5.. run return 0
schedule clear stewbeet_summit:walls/qol_ecosystem/fade_out_down
schedule clear stewbeet_summit:walls/qol_ecosystem/fade_swap_down
schedule clear stewbeet_summit:walls/qol_ecosystem/fade_in_down
schedule clear stewbeet_summit:walls/qol_ecosystem/fade_out_up
schedule clear stewbeet_summit:walls/qol_ecosystem/fade_swap_up
schedule clear stewbeet_summit:walls/qol_ecosystem/fade_in_up
scoreboard players add #qol_ecosystem stewbeet_summit.page 1
data merge entity 20180612-2026-2002-2098-202200000009 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/qol_ecosystem/pop_settle 2t replace
scoreboard players set #qol_ecosystem stewbeet_summit.fc 2
function stewbeet_summit:walls/qol_ecosystem/fade_out_down

