
#> stewbeet_summit:walls/custom_blocks_made_easy/page_0
#
# @within	stewbeet_summit:walls/custom_blocks_made_easy/show
#

# Page 1/6 "The Block Class": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000004 text set value ["", {"text": "Define a block (1/6)\n\n", "bold": true, "color": "gold"}, ["", {"text": "Block", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "id", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"ruby_ore\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "vanilla_block", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "VanillaBlock", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "id", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"minecraft:stone\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "no_silk_touch_drop", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"ruby\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": ")", "color": "#F8F8F2"}]]
data modify entity 20180612-2026-2002-2098-202000000004 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000004 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000004 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000004 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000004 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000004 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000004 height set value 0.0f

