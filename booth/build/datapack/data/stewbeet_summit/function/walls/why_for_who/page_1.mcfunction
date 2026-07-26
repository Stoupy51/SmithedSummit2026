
#> stewbeet_summit:walls/why_for_who/page_1
#
# @within	stewbeet_summit:walls/why_for_who/show
#

# Page 2/4 "For Beginners": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000001 text set value ["", {"text": "Friendly for newcomers (2/4)\n\n", "bold": true, "color": "gold"}, {"text": "Sensible defaults and ready templates: minimal, basic, extensive.\n\n", "color": "white"}, {"text": "stewbeet init basic\n\n", "color": "#8BE9FD"}, {"text": "Up and running in seconds.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000001 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000001 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000001 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000001 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

