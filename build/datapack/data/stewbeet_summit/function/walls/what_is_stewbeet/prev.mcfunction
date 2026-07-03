
#> stewbeet_summit:walls/what_is_stewbeet/prev
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 211.5 101.0 -18.5 & rotated 90 0 ]
#

scoreboard players remove #what_is_stewbeet stewbeet_summit.page 1
execute if score #what_is_stewbeet stewbeet_summit.page matches ..-1 run scoreboard players set #what_is_stewbeet stewbeet_summit.page 0
function stewbeet_summit:walls/what_is_stewbeet/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
data merge entity 20180612-2026-2002-2098-202100000000 {interpolation_duration:0,start_interpolation:0,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/what_is_stewbeet/pop_settle 2t replace

