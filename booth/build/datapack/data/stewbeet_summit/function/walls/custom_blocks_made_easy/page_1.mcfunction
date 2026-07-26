
#> stewbeet_summit:walls/custom_blocks_made_easy/page_1
#
# @within	stewbeet_summit:walls/custom_blocks_made_easy/show
#

# Page 2/6 "Placement & Breaking": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000004 text set value ["", {"text": "It just works (2/6)\n\n", "bold": true, "color": "gold"}, {"text": "Placement and destruction are handled for you through ", "color": "white"}, {"text": "Smithed Custom Blocks", "bold": true, "color": "aqua"}, {"text": " and optimized loops.\n\n", "color": "white"}, {"text": "No manual interaction entities.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000004 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000004 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000004 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000004 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000004 height set value 0.0f

