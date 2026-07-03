
#> stewbeet_summit:walls/why_for_who/prev
#
# @executed	positioned 204.5 101.0 -22.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 204.5 101.0 -22.5 & rotated 0 0 ]
#

scoreboard players remove #why_for_who stewbeet_summit.page 1
execute if score #why_for_who stewbeet_summit.page matches ..-1 run scoreboard players set #why_for_who stewbeet_summit.page 0
function stewbeet_summit:walls/why_for_who/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2
data merge entity 20180612-2026-2002-2098-202100000001 {interpolation_duration:0,start_interpolation:0,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/why_for_who/pop_settle 2t replace

