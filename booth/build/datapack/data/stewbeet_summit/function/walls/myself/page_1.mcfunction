
#> stewbeet_summit:walls/myself/page_1
#
# @within	stewbeet_summit:walls/myself/show
#

# Page 2/3 "Jobs": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000014 text set value ["", {"text": "Jobs (2/3)\n\n", "bold": true, "color": "gold"}, {"text": "- ", "color": "white"}, {"text": "Data Scientist", "bold": true, "color": "aqua"}, {"text": " in Health,\nas a full-time job IRL\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "Sys Admin", "bold": true, "color": "aqua"}, {"text": " of Survisland,\na Survivor (TV-show) like community\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "Administrator", "bold": true, "color": "aqua"}, {"text": " of Paralya,\na french-speaking Minecraft commuinity\n", "color": "white"}, {"text": "- 23 years old, ", "color": "white"}, {"text": "French ", "bold": true, "color": "gold"}, {"text": "(unfortunately)", "color": "#7F8C99", "italic": true, "strikethrough": true}, {"text": "\n", "color": "white"}, {"text": "- Speaking English, French and 日本語", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000014 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000014 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000014 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000014 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000014 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000014 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000014 height set value 0.0f

