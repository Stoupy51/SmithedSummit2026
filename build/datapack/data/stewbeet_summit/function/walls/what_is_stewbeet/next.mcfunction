
#> stewbeet_summit:walls/what_is_stewbeet/next
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 211.5 101.0 -18.5 & rotated 90 0 ]
#

playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
execute if score #what_is_stewbeet stewbeet_summit.page matches 3.. run return 0
schedule clear stewbeet_summit:walls/what_is_stewbeet/fade_out_down
schedule clear stewbeet_summit:walls/what_is_stewbeet/fade_swap_down
schedule clear stewbeet_summit:walls/what_is_stewbeet/fade_in_down
schedule clear stewbeet_summit:walls/what_is_stewbeet/fade_out_up
schedule clear stewbeet_summit:walls/what_is_stewbeet/fade_swap_up
schedule clear stewbeet_summit:walls/what_is_stewbeet/fade_in_up
scoreboard players add #what_is_stewbeet stewbeet_summit.page 1
data merge entity 20180612-2026-2002-2098-202200000000 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/what_is_stewbeet/pop_settle 2t replace
scoreboard players set #what_is_stewbeet stewbeet_summit.fc 2
function stewbeet_summit:walls/what_is_stewbeet/fade_out_down

