
#> stewbeet_summit:v0.0.1/load/confirm_load
#
# @within	stewbeet_summit:v0.0.1/load/valid_dependencies
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded StewBeet Summit 2026 v0.0.1]","color":"green"}
scoreboard players set #stewbeet_summit.loaded load.status 1
function stewbeet_summit:v0.0.1/load/set_items_storage

# Entrance decorations (StewBeet)
kill @e[tag=stewbeet_summit.entity]
function stewbeet_summit:intro/setup

# Presentation walls (StewBeet)
scoreboard objectives add stewbeet_summit.page dummy
kill @e[tag=stewbeet_summit.wall]
function stewbeet_summit:walls/setup
function stewbeet_summit:walls/reset

