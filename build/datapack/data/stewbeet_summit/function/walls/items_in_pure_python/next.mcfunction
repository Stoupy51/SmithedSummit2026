
#> stewbeet_summit:walls/items_in_pure_python/next
#
# @executed	positioned 196.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 196.5 101.0 -11.5 & rotated 180 0 ]
#

playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
execute if score #items_in_pure_python stewbeet_summit.page matches 4.. run return 0
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_out_down
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_swap_down
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_in_down
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_out_up
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_swap_up
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_in_up
scoreboard players add #items_in_pure_python stewbeet_summit.page 1
data merge entity 20180612-2026-2002-2098-202200000003 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/items_in_pure_python/pop_settle 2t replace
scoreboard players set #items_in_pure_python stewbeet_summit.fc 2
function stewbeet_summit:walls/items_in_pure_python/fade_out_down

