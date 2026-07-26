
#> stewbeet_summit:walls/standing_on_giants/next
#
# @executed	positioned 194.5 101.0 -19.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 194.5 101.0 -19.5 & rotated 90 0 ]
#

# Click sound for nearby players
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

# Boundary guard: already on the last page (the right arrow is grayed), do nothing
execute if score #standing_on_giants stewbeet_summit.page matches 6.. run return 0

# Cancel any fade chain still in flight so a fast second click can't leave two running
schedule clear stewbeet_summit:walls/standing_on_giants/fade_out_down
schedule clear stewbeet_summit:walls/standing_on_giants/fade_swap_down
schedule clear stewbeet_summit:walls/standing_on_giants/fade_in_down
schedule clear stewbeet_summit:walls/standing_on_giants/fade_out_up
schedule clear stewbeet_summit:walls/standing_on_giants/fade_swap_up
schedule clear stewbeet_summit:walls/standing_on_giants/fade_in_up

# Advance the page index (the text swap itself happens later, in fade_swap)
scoreboard players add #standing_on_giants stewbeet_summit.page 1

# Click feedback: snap the clicked arrow to its popped size now, ease it back next tick
data merge entity 20180612-2026-2002-2098-202200000005 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/standing_on_giants/pop_settle 2t replace

# Kick off the page fade: arm the phase counter and run the first fade-out frame now
scoreboard players set #standing_on_giants stewbeet_summit.data 2
function stewbeet_summit:walls/standing_on_giants/fade_out_down

