
#> stewbeet_summit:walls/custom_blocks_made_easy/page_2
#
# @within	stewbeet_summit:walls/custom_blocks_made_easy/show
#

# Page 3/6 "Ores Done Right": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000004 text set value ["", {"text": "One line = a real ore (3/6)\n\n", "bold": true, "color": "gold"}, {"text": "That single ", "color": "white"}, {"text": "no_silk_touch_drop", "bold": true, "color": "aqua"}, {"text": " line gives the block true ore behavior:\n\n- ", "color": "white"}, {"text": "Silk Touch", "bold": true, "color": "aqua"}, {"text": " -> drops the block\n- otherwise -> drops your item (", "color": "white"}, {"text": "ruby", "bold": true, "color": "aqua"}, {"text": ")\n- ", "color": "white"}, {"text": "Fortune", "bold": true, "color": "aqua"}, {"text": " multiplies the count, like vanilla ores do\n\n", "color": "white"}, {"text": "Wired via Common Signals. Pass a full LootTable instead for random drops.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000004 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000004 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000004 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000004 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000004 height set value 0.0f

