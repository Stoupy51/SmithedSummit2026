
#> stewbeet_summit:walls/wip_datapacks/fade_out_up
#
# @executed	positioned 198.5 53.0 -13.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/wip_datapacks/fade_out_up 1t replace [ scheduled ]
#			stewbeet_summit:walls/wip_datapacks/prev
#

# Fade out (up): while the counter (#wip_datapacks stewbeet_summit.data) ticks 2->0, ramp the text
# full->invisible and slide it towards its exit side, one exact frame per counter value
execute if score #wip_datapacks stewbeet_summit.data matches 2 run data merge entity 20180612-2026-2002-2098-202000000013 {interpolation_duration:4,start_interpolation:-1,text_opacity:-1b,background:1073741824,transformation:{translation:[0f,0.0f,0f]}}
execute if score #wip_datapacks stewbeet_summit.data matches 1 run data merge entity 20180612-2026-2002-2098-202000000013 {interpolation_duration:4,start_interpolation:-1,text_opacity:-124b,background:536870912,transformation:{translation:[0f,0.075f,0f]}}
execute if score #wip_datapacks stewbeet_summit.data matches 0 run data merge entity 20180612-2026-2002-2098-202000000013 {interpolation_duration:4,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,0.15f,0f]}}

# Counter at 0: the text is invisible, hand off to fade_swap next tick (via schedule, NOT
# an inline call: fade_swap resets the counter, which would re-arm the guards below)
execute if score #wip_datapacks stewbeet_summit.data matches 0 run schedule function stewbeet_summit:walls/wip_datapacks/fade_swap_up 1t replace

# Otherwise: re-run this function next tick and count down
execute if score #wip_datapacks stewbeet_summit.data matches 1.. run schedule function stewbeet_summit:walls/wip_datapacks/fade_out_up 1t replace
execute if score #wip_datapacks stewbeet_summit.data matches 1.. run scoreboard players remove #wip_datapacks stewbeet_summit.data 1

