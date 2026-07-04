
#> stewbeet_summit:walls/material_sets/fade_in_up
#
# @within	stewbeet_summit:walls/material_sets/fade_swap_up 1t replace [ scheduled ]
#			stewbeet_summit:walls/material_sets/fade_in_up 1t replace [ scheduled ]
#

# Fade in (up): while the counter (#material_sets stewbeet_summit.fc) ticks 2->0, ramp the new text
# invisible->full while it slides from its entry side back to center
execute if score #material_sets stewbeet_summit.fc matches 2 run data merge entity 20180612-2026-2002-2098-202000000007 {interpolation_duration:4,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,-0.15f,0f]}}
execute if score #material_sets stewbeet_summit.fc matches 1 run data merge entity 20180612-2026-2002-2098-202000000007 {interpolation_duration:4,start_interpolation:-1,text_opacity:-124b,background:536870912,transformation:{translation:[0f,-0.075f,0f]}}
execute if score #material_sets stewbeet_summit.fc matches 0 run data merge entity 20180612-2026-2002-2098-202000000007 {interpolation_duration:4,start_interpolation:-1,text_opacity:-1b,background:1073741824,transformation:{translation:[0f,-0.0f,0f]}}

# Re-run this function next tick and count down until the counter reaches 0
execute if score #material_sets stewbeet_summit.fc matches 1.. run schedule function stewbeet_summit:walls/material_sets/fade_in_up 1t replace
execute if score #material_sets stewbeet_summit.fc matches 1.. run scoreboard players remove #material_sets stewbeet_summit.fc 1

