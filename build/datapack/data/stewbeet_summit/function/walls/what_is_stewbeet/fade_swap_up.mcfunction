
#> stewbeet_summit:walls/what_is_stewbeet/fade_swap_up
#
# @within	stewbeet_summit:walls/what_is_stewbeet/fade_out_up 1t replace [ scheduled ]
#

function stewbeet_summit:walls/what_is_stewbeet/show
data merge entity 20180612-2026-2002-2098-202000000000 {interpolation_duration:0,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,-0.15f,0f]}}
scoreboard players set #what_is_stewbeet stewbeet_summit.fc 2
schedule function stewbeet_summit:walls/what_is_stewbeet/fade_in_up 1t replace

