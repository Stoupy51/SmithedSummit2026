
#> stewbeet_summit:walls/custom_blocks_made_easy/fade_swap_down
#
# @within	stewbeet_summit:walls/custom_blocks_made_easy/fade_out_down 1t replace [ scheduled ]
#

function stewbeet_summit:walls/custom_blocks_made_easy/show
data merge entity 20180612-2026-2002-2098-202000000004 {interpolation_duration:0,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,0.15f,0f]}}
scoreboard players set #custom_blocks_made_easy stewbeet_summit.fc 2
schedule function stewbeet_summit:walls/custom_blocks_made_easy/fade_in_down 1t replace

