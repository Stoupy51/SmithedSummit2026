
#> stewbeet_summit:walls/items_in_pure_python/prev
#
# @executed	positioned 196.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 196.5 101.0 -11.5 & rotated 180 0 ]
#

# Click sound for nearby players (slightly lower pitch than next)
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

# Boundary guard: already on the first page (the left arrow is grayed), do nothing
execute if score #items_in_pure_python stewbeet_summit.page matches ..0 run return 0

# Cancel any fade chain still in flight so a fast second click can't leave two running
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_out_down
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_swap_down
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_in_down
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_out_up
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_swap_up
schedule clear stewbeet_summit:walls/items_in_pure_python/fade_in_up

# Rewind the page index (the text swap itself happens later, in fade_swap)
scoreboard players remove #items_in_pure_python stewbeet_summit.page 1

# Click feedback: snap the clicked arrow to its popped size now, ease it back next tick
data merge entity 20180612-2026-2002-2098-202100000003 {interpolation_duration:0,start_interpolation:-1,transformation:{scale:[1.25f,1.25f,1.25f]}}
schedule function stewbeet_summit:walls/items_in_pure_python/pop_settle 2t replace

# Kick off the page fade: arm the phase counter and run the first fade-out frame now
scoreboard players set #items_in_pure_python stewbeet_summit.fc 2
function stewbeet_summit:walls/items_in_pure_python/fade_out_up

