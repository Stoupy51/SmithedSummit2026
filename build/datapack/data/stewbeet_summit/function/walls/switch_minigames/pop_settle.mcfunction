
#> stewbeet_summit:walls/switch_minigames/pop_settle
#
# @within	stewbeet_summit:walls/switch_minigames/next 2t replace [ scheduled ]
#			stewbeet_summit:walls/switch_minigames/prev 2t replace [ scheduled ]
#

# Ease both arrows back to normal size over 8 ticks
# (the un-clicked arrow is already at normal size, so its interpolation is a no-op)
data merge entity 20180612-2026-2002-2098-202100000011 {interpolation_duration:8,start_interpolation:-1,transformation:{scale:[1.0f,1.0f,1.0f]}}
data merge entity 20180612-2026-2002-2098-202200000011 {interpolation_duration:8,start_interpolation:-1,transformation:{scale:[1.0f,1.0f,1.0f]}}

