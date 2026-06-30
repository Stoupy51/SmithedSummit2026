
#> stewbeet_summit:walls/zone3/page2
#
# @within	stewbeet_summit:walls/zone3/show
#

data modify entity 20180612-2026-2002-2098-202000000003 text set value ["", {"text": "Just drop a texture\n\n", "bold": true, "color": "gold"}, {"text": "Put ", "color": "white"}, {"text": "ruby.png", "bold": true, "color": "aqua"}, {"text": " in assets/textures/\n\n", "color": "white"}, {"text": "StewBeet auto-detects it and builds\n", "color": "white"}, {"text": "the model + item_model reference.\n\n", "color": "white"}, {"text": "No JSON model files by hand.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000003 line_width set value 175
data modify entity 20180612-2026-2002-2098-202100000003 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000003 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

