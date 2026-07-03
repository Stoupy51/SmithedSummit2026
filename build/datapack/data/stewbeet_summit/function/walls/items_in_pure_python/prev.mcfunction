
#> stewbeet_summit:walls/items_in_pure_python/prev
#
# @executed	positioned 196.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 196.5 101.0 -11.5 & rotated 180 0 ]
#

scoreboard players remove #items_in_pure_python stewbeet_summit.page 1
execute if score #items_in_pure_python stewbeet_summit.page matches ..-1 run scoreboard players set #items_in_pure_python stewbeet_summit.page 0
function stewbeet_summit:walls/items_in_pure_python/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
data merge entity 20180612-2026-2002-2098-202100000003 {interpolation_duration:0,start_interpolation:0,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/items_in_pure_python/pop_settle 2t replace

