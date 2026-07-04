
#> stewbeet_summit:v0.0.1/load/confirm_load
#
# @within	stewbeet_summit:v0.0.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded StewBeet Summit 2026 v0.0.1]","color":"green"}
scoreboard players set #stewbeet_summit.loaded load.status 1

# Booth entities (StewBeet): entrance decorations + presentation walls
function stewbeet_summit:entities/summon

