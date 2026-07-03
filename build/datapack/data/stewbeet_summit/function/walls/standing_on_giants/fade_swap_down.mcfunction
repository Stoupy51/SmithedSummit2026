
#> stewbeet_summit:walls/standing_on_giants/fade_swap_down
#
# @within	stewbeet_summit:walls/standing_on_giants/fade_out_down 1t replace [ scheduled ]
#

function stewbeet_summit:walls/standing_on_giants/show
data merge entity 20180612-2026-2002-2098-202000000005 {interpolation_duration:0,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,0.15f,0f]}}
scoreboard players set #standing_on_giants stewbeet_summit.fc 2
schedule function stewbeet_summit:walls/standing_on_giants/fade_in_down 1t replace

