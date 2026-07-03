
#> stewbeet_summit:walls/custom_blocks_made_easy/next
#
# @executed	positioned 191.5 101.0 -16.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 191.5 101.0 -16.5 & rotated -90 0 ]
#

scoreboard players add #custom_blocks_made_easy stewbeet_summit.page 1
execute if score #custom_blocks_made_easy stewbeet_summit.page matches 6.. run scoreboard players set #custom_blocks_made_easy stewbeet_summit.page 5
function stewbeet_summit:walls/custom_blocks_made_easy/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5
data merge entity 20180612-2026-2002-2098-202200000004 {interpolation_duration:0,start_interpolation:0,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/custom_blocks_made_easy/pop_settle 2t replace

