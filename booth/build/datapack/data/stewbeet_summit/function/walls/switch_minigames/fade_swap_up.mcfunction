
#> stewbeet_summit:walls/switch_minigames/fade_swap_up
#
# @within	stewbeet_summit:walls/switch_minigames/fade_out_up 1t replace [ scheduled ]
#

# The old text is now invisible: swap the new page in, then snap it (duration 0, still
# invisible) to its entry side so it doesn't visibly glide across from the exit side
function stewbeet_summit:walls/switch_minigames/show
data merge entity 20180612-2026-2002-2098-202000000011 {interpolation_duration:0,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,-0.15f,0f]}}

# Re-arm the phase counter and start the fade-in next tick
scoreboard players set #switch_minigames stewbeet_summit.data 2
schedule function stewbeet_summit:walls/switch_minigames/fade_in_up 1t replace

