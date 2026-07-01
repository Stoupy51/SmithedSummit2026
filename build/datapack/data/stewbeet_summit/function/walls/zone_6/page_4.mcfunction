
#> stewbeet_summit:walls/zone_6/page_4
#
# @within	stewbeet_summit:walls/zone_6/show
#

data modify entity 20180612-2026-2002-2098-202000000006 text set value ["", {"text": "Results your way (5/6)\n\n", "bold": true, "color": "gold"}, {"text": "The result is the item you're defining by default - but you can bend it:\n\n", "color": "white"}, {"text": "result_count=8             # bulk\n", "color": "#8BE9FD"}, {"text": "result=Ingr(\"bone_meal\") # other item\n", "color": "#8BE9FD"}, {"text": "result_count={              # random!\n", "color": "#8BE9FD"}, {"text": "    \"type\":\"minecraft:uniform\",\n", "color": "#8BE9FD"}, {"text": "    \"min\":4, \"max\":6,\n", "color": "#8BE9FD"}, {"text": "}\n\n", "color": "#8BE9FD"}, {"text": "Perfect for ore-crushing and drops.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000006 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000006 transformation.scale set value [0.45, 0.45, 0.45]
data modify entity 20180612-2026-2002-2098-202100000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

