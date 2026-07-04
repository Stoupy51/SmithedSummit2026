
#> stewbeet_summit:walls/items_in_pure_python/fade_swap_down
#
# @within	stewbeet_summit:walls/items_in_pure_python/fade_out_down 1t replace [ scheduled ]
#

# The old text is now invisible: swap the new page in, then snap it (duration 0, still
# invisible) to its entry side so it doesn't visibly glide across from the exit side
function stewbeet_summit:walls/items_in_pure_python/show
data merge entity 20180612-2026-2002-2098-202000000003 {interpolation_duration:0,start_interpolation:-1,text_opacity:10b,background:0,transformation:{translation:[0f,0.15f,0f]}}

# Re-arm the phase counter and start the fade-in next tick
scoreboard players set #items_in_pure_python stewbeet_summit.data 2
schedule function stewbeet_summit:walls/items_in_pure_python/fade_in_down 1t replace

