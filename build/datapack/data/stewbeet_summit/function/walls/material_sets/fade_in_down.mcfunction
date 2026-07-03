
#> stewbeet_summit:walls/material_sets/fade_in_down
#
# @within	stewbeet_summit:walls/material_sets/fade_swap_down 1t replace [ scheduled ]
#			stewbeet_summit:walls/material_sets/fade_in_down 1t replace [ scheduled ]
#

execute if score #material_sets stewbeet_summit.fc matches 2 run data merge entity 20180612-2026-2002-2098-202000000007 {interpolation_duration:4,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,0.15f,0f]}}
execute if score #material_sets stewbeet_summit.fc matches 1 run data merge entity 20180612-2026-2002-2098-202000000007 {interpolation_duration:4,start_interpolation:-1,text_opacity:-124b,background:536870912,transformation:{translation:[0f,0.075f,0f]}}
execute if score #material_sets stewbeet_summit.fc matches 0 run data merge entity 20180612-2026-2002-2098-202000000007 {interpolation_duration:4,start_interpolation:-1,text_opacity:-1b,background:1073741824,transformation:{translation:[0f,0.0f,0f]}}
execute if score #material_sets stewbeet_summit.fc matches 1.. run schedule function stewbeet_summit:walls/material_sets/fade_in_down 1t replace
execute if score #material_sets stewbeet_summit.fc matches 1.. run scoreboard players remove #material_sets stewbeet_summit.fc 1

