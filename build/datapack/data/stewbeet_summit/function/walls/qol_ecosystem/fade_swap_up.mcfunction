
#> stewbeet_summit:walls/qol_ecosystem/fade_swap_up
#
# @within	stewbeet_summit:walls/qol_ecosystem/fade_out_up 1t replace [ scheduled ]
#

function stewbeet_summit:walls/qol_ecosystem/show
data merge entity 20180612-2026-2002-2098-202000000009 {interpolation_duration:0,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,-0.15f,0f]}}
scoreboard players set #qol_ecosystem stewbeet_summit.fc 2
schedule function stewbeet_summit:walls/qol_ecosystem/fade_in_up 1t replace

