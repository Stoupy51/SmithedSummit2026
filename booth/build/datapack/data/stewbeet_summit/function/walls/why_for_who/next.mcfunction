
#> stewbeet_summit:walls/why_for_who/next
#
# @executed	positioned 204.5 101.0 -22.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 204.5 101.0 -22.5 & rotated 0 0 ]
#

# Click sound for nearby players
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

# Boundary guard: already on the last page (the right arrow is grayed), do nothing
execute if score #why_for_who stewbeet_summit.page matches 3.. run return 0

# Cancel any fade chain still in flight so a fast second click can't leave two running
schedule clear stewbeet_summit:walls/why_for_who/fade_out_down
schedule clear stewbeet_summit:walls/why_for_who/fade_swap_down
schedule clear stewbeet_summit:walls/why_for_who/fade_in_down
schedule clear stewbeet_summit:walls/why_for_who/fade_out_up
schedule clear stewbeet_summit:walls/why_for_who/fade_swap_up
schedule clear stewbeet_summit:walls/why_for_who/fade_in_up

# Advance the page index (the text swap itself happens later, in fade_swap)
scoreboard players add #why_for_who stewbeet_summit.page 1

# Click feedback: snap the clicked arrow to its popped size now, ease it back next tick
data merge entity 20180612-2026-2002-2098-202200000001 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/why_for_who/pop_settle 2t replace

# Kick off the page fade: arm the phase counter and run the first fade-out frame now
scoreboard players set #why_for_who stewbeet_summit.data 2
function stewbeet_summit:walls/why_for_who/fade_out_down

