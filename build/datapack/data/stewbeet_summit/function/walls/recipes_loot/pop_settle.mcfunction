
#> stewbeet_summit:walls/recipes_loot/pop_settle
#
# @within	stewbeet_summit:walls/recipes_loot/next 2t replace [ scheduled ]
#			stewbeet_summit:walls/recipes_loot/prev 2t replace [ scheduled ]
#

# Ease both arrows back to normal size over 8 ticks
# (the un-clicked arrow is already at normal size, so its interpolation is a no-op)
data merge entity 20180612-2026-2002-2098-202100000006 {interpolation_duration:8,start_interpolation:-1,transformation:{scale:[1.0f,1.0f,1.0f]}}
data merge entity 20180612-2026-2002-2098-202200000006 {interpolation_duration:8,start_interpolation:-1,transformation:{scale:[1.0f,1.0f,1.0f]}}

