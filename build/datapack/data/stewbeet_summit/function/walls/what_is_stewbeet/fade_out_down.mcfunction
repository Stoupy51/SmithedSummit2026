
#> stewbeet_summit:walls/what_is_stewbeet/fade_out_down
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/what_is_stewbeet/fade_out_down 1t replace [ scheduled ]
#			stewbeet_summit:walls/what_is_stewbeet/next
#

execute if score #what_is_stewbeet stewbeet_summit.fc matches 2 run data merge entity 20180612-2026-2002-2098-202000000000 {interpolation_duration:4,start_interpolation:-1,text_opacity:-1b,background:1073741824,transformation:{translation:[0f,-0.0f,0f]}}
execute if score #what_is_stewbeet stewbeet_summit.fc matches 1 run data merge entity 20180612-2026-2002-2098-202000000000 {interpolation_duration:4,start_interpolation:-1,text_opacity:-124b,background:536870912,transformation:{translation:[0f,-0.075f,0f]}}
execute if score #what_is_stewbeet stewbeet_summit.fc matches 0 run data merge entity 20180612-2026-2002-2098-202000000000 {interpolation_duration:4,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,-0.15f,0f]}}
execute if score #what_is_stewbeet stewbeet_summit.fc matches 0 run schedule function stewbeet_summit:walls/what_is_stewbeet/fade_swap_down 1t replace
execute if score #what_is_stewbeet stewbeet_summit.fc matches 1.. run schedule function stewbeet_summit:walls/what_is_stewbeet/fade_out_down 1t replace
execute if score #what_is_stewbeet stewbeet_summit.fc matches 1.. run scoreboard players remove #what_is_stewbeet stewbeet_summit.fc 1

