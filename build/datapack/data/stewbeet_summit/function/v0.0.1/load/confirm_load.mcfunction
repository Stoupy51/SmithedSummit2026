
#> stewbeet_summit:v0.0.1/load/confirm_load
#
# @within	stewbeet_summit:v0.0.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded StewBeet Summit 2026 v0.0.1]","color":"green"}
scoreboard players set #stewbeet_summit.loaded load.status 1
function stewbeet_summit:v0.0.1/load/set_items_storage

# Summon a Black Hole underground
summon minecraft:item_display 198.5 54.0 -21.5 {"item": {"id": "minecraft:stone", "components": {"minecraft:item_model": "stewbeet_summit:black_hole"}, "count": 1}, "transformation": {"left_rotation": [0.0, 0.0, 0.0, 1.0], "right_rotation": [0.0, 0.0, 0.0, 1.0], "scale": [16.69, 9.69, -18.69], "translation": [0.0, 0.0, 0.0]}}

