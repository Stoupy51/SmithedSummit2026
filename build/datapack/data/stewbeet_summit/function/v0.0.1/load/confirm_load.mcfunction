
#> stewbeet_summit:v0.0.1/load/confirm_load
#
# @within	stewbeet_summit:v0.0.1/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded StewBeet Summit 2026 v0.0.1]","color":"green"}
scoreboard players set #stewbeet_summit.loaded load.status 1
function stewbeet_summit:v0.0.1/load/set_items_storage

# TODO: remove
kill @e[tag=stewbeet_summit.static]

# Summon a Black Hole underground
execute unless entity 20180612-2026-2002-2098-201000000000 run summon minecraft:item_display 198.5 54.0 -21.5 {UUID:uuid("20180612-2026-2002-2098-201000000000"),"item": {"id": "stone", "components": {"minecraft:item_model": "stewbeet_summit:bg_black_hole"}, "count": 1}, "Tags": ["stewbeet_summit.bg_black_hole", "stewbeet_summit.static", "summit.static"], "brightness": {"block": 15, "sky": 15}, "transformation": {"left_rotation": [0.0, 0.0, 0.0, 1.0], "right_rotation": [0.0, 0.0, 0.0, 1.0], "scale": [16.69, 9.69, -18.69], "translation": [0.0, 0.0, 0.0]}}

# Summon the logo, title, and arrow at entrance
execute unless entity 20180612-2026-2002-2098-201000000001 run summon minecraft:item_display 196.5 103.5 -9.9 {UUID:uuid("20180612-2026-2002-2098-201000000001"),"item": {"id": "stone", "components": {"minecraft:item_model": "stewbeet_summit:logo"}, "count": 1}, "Tags": ["stewbeet_summit.logo", "stewbeet_summit.static", "summit.static"], "brightness": {"block": 15, "sky": 15}, "transformation": {"left_rotation": [0.0, 0.0, 0.0, 1.0], "right_rotation": [0.0, 0.0, 0.0, 1.0], "scale": [2.5, 2.5, 4.0], "translation": [0.0, 0.0, 0.0]}, "Rotation": [180, 0]}
execute unless entity 20180612-2026-2002-2098-201000000002 run summon minecraft:item_display 196.5 103.0 -9.6 {UUID:uuid("20180612-2026-2002-2098-201000000002"),"item": {"id": "stone", "components": {"minecraft:item_model": "stewbeet_summit:title"}, "count": 1}, "Tags": ["stewbeet_summit.title", "stewbeet_summit.static", "summit.static"], "brightness": {"block": 15, "sky": 15}, "transformation": {"left_rotation": [0.0, 0.0, 0.0, 1.0], "right_rotation": [0.0, 0.0, 0.0, 1.0], "scale": [3.5, 3.5, 3.5], "translation": [0.0, 0.0, 0.0]}, "Rotation": [0, 0]}
execute unless entity 20180612-2026-2002-2098-201000000003 run summon minecraft:item_display 197.6875 99.4375 -10.5 {UUID:uuid("20180612-2026-2002-2098-201000000003"),"item": {"id": "stone", "components": {"minecraft:item_model": "stewbeet_summit:arrow"}, "count": 1}, "Tags": ["stewbeet_summit.arrow", "stewbeet_summit.static", "summit.static"], "brightness": {"block": 15, "sky": 15}, "transformation": {"left_rotation": [0.0, 0.0, 0.172, 0.985], "right_rotation": [0.0, 0.0, 0.0, 1.0], "scale": [5.0, 5.0, 5.0], "translation": [0.0, 0.0, 0.0]}}
execute unless entity 20180612-2026-2002-2098-201000000004 run summon minecraft:item_display 198.9375 98.125 -4.0 {UUID:uuid("20180612-2026-2002-2098-201000000004"),"item": {"id": "stone", "components": {"minecraft:item_model": "stewbeet_summit:arrow"}, "count": 1}, "Tags": ["stewbeet_summit.arrow", "stewbeet_summit.static", "summit.static"], "brightness": {"block": 15, "sky": 15}, "transformation": {"left_rotation": [0.0, 0.0, 0.0, 1.0], "right_rotation": [0.0, 0.0, 0.0, 1.0], "scale": [5.0, 5.0, 2.5], "translation": [0.0, 0.0, 0.0]}, "Rotation": [-90, 0]}

