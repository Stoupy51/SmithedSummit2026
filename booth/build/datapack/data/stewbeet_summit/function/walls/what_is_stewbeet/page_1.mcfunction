
#> stewbeet_summit:walls/what_is_stewbeet/page_1
#
# @within	stewbeet_summit:walls/what_is_stewbeet/show
#

# Page 2/4 "The Problem": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000000 text set value ["", {"text": "The old way (2/4)\n\n", "bold": true, "color": "gold"}, {"text": "A modern datapack means hundreds of hand-written files: models, loot tables, recipes, lang, item components...\n\n", "color": "white"}, {"text": "Tedious. Error-prone. Hard to maintain.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000000 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000000 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000000 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000000 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000000 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000000 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000000 height set value 0.0f

