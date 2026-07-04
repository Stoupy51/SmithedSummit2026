
#> stewbeet_summit:walls/why_for_who/page_2
#
# @within	stewbeet_summit:walls/why_for_who/show
#

# Page 3/4 "For Veterans": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000001 text set value ["", {"text": "Powerful for experts (3/4)\n\n", "bold": true, "color": "gold"}, {"text": "Drop down to raw ", "color": "white"}, {"text": "beet", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "bolt", "bold": true, "color": "aqua"}, {"text": ", and ", "color": "white"}, {"text": "mecha", "bold": true, "color": "aqua"}, {"text": " whenever you want.\n\nOverride or ", "color": "white"}, {"text": "merge", "bold": true, "color": "gold"}, {"text": " any generated file.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000001 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000001 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000001 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000001 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

