
#> stewbeet_summit:walls/material_sets/show
#
# @within	stewbeet_summit:walls/material_sets/fade_swap_down
#			stewbeet_summit:walls/material_sets/fade_swap_up
#			stewbeet_summit:walls/reset
#

# Refresh this wall: run the page function matching the current page index (#material_sets)
execute if score #material_sets stewbeet_summit.page matches 0 run return run function stewbeet_summit:walls/material_sets/page_0
execute if score #material_sets stewbeet_summit.page matches 1 run return run function stewbeet_summit:walls/material_sets/page_1
execute if score #material_sets stewbeet_summit.page matches 2 run return run function stewbeet_summit:walls/material_sets/page_2
execute if score #material_sets stewbeet_summit.page matches 3 run return run function stewbeet_summit:walls/material_sets/page_3
execute if score #material_sets stewbeet_summit.page matches 4 run return run function stewbeet_summit:walls/material_sets/page_4
execute if score #material_sets stewbeet_summit.page matches 5 run return run function stewbeet_summit:walls/material_sets/page_5
execute if score #material_sets stewbeet_summit.page matches 6 run return run function stewbeet_summit:walls/material_sets/page_6
execute if score #material_sets stewbeet_summit.page matches 7 run return run function stewbeet_summit:walls/material_sets/page_7
execute if score #material_sets stewbeet_summit.page matches 8 run return run function stewbeet_summit:walls/material_sets/page_8

