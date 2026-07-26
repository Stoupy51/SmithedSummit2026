
#> stewbeet_summit:walls/why_for_who/page_3
#
# @within	stewbeet_summit:walls/why_for_who/show
#

# Page 4/4 "Battle-Tested": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000001 text set value ["", {"text": "Used in real projects (4/4)\n\n", "bold": true, "color": "gold"}, {"text": "- SimplEnergy\n- LifeStealFR\n- Stardust Fragment\n- and many more\n\n", "color": "white"}, {"text": "Your next project here!", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000001 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000001 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000001 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000001 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

