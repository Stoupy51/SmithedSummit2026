
#> stewbeet_summit:walls/zone4/page2
#
# @within	stewbeet_summit:walls/zone4/show
#

data modify entity 20180612-2026-2002-2098-202000000004 text set value ["", {"text": "One line = a real ore (3/6)\n\n", "bold": true, "color": "gold"}, {"text": "That single ", "color": "white"}, {"text": "no_silk_touch_drop", "bold": true, "color": "aqua"}, {"text": " line gives the block true ore behavior:\n\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "Silk Touch", "bold": true, "color": "aqua"}, {"text": " -> drops the block\n", "color": "white"}, {"text": "- otherwise -> drops your item (", "color": "white"}, {"text": "ruby", "bold": true, "color": "aqua"}, {"text": ")\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "Fortune", "bold": true, "color": "aqua"}, {"text": " multiplies the count, like\n  vanilla ores do\n\n", "color": "white"}, {"text": "Wired via Common Signals. Pass a full LootTable instead for random drops.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000004 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000004 transformation.scale set value [0.5, 0.5, 0.5]
data modify entity 20180612-2026-2002-2098-202100000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

