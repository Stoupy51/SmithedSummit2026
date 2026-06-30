
#> stewbeet_summit:walls/zone4/page4
#
# @within	stewbeet_summit:walls/zone4/show
#

data modify entity 20180612-2026-2002-2098-202000000004 text set value ["", {"text": "Texture name patterns (5/6)\n\n", "bold": true, "color": "gold"}, {"text": "StewBeet tries to auto-detect the textures for you and check for patterns:\n\n", "color": "white"}, {"text": "front+side+top+bottom", "bold": true, "color": "aqua"}, {"text": " -> furnace\n", "color": "white"}, {"text": "bottom+side+top", "bold": true, "color": "aqua"}, {"text": " -> barrel\n", "color": "white"}, {"text": "end+side", "bold": true, "color": "aqua"}, {"text": " -> pillar\n", "color": "white"}, {"text": "bottom+side+top+inner", "bold": true, "color": "aqua"}, {"text": " -> cake\n\n", "color": "white"}, {"text": "One texture -> cube_all.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000004 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000004 transformation.scale set value [0.5, 0.5, 0.5]
data modify entity 20180612-2026-2002-2098-202100000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

