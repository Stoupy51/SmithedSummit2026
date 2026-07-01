
#> stewbeet_summit:walls/custom_blocks_made_easy/prev
#
# @executed	positioned 191.5 101.0 -16.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 191.5 101.0 -16.5 & rotated -90 0 ]
#

scoreboard players remove #custom_blocks_made_easy stewbeet_summit.page 1
execute if score #custom_blocks_made_easy stewbeet_summit.page matches ..-1 run scoreboard players set #custom_blocks_made_easy stewbeet_summit.page 0
function stewbeet_summit:walls/custom_blocks_made_easy/show
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

