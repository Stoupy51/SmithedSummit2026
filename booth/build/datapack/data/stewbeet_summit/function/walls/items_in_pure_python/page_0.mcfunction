
#> stewbeet_summit:walls/items_in_pure_python/page_0
#
# @within	stewbeet_summit:walls/items_in_pure_python/show
#

# Page 1/5 "The Item Class": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000003 text set value ["", {"text": "Define an item (1/5)\n\n", "bold": true, "color": "gold"}, {"text": "Here is a very simple item definition:\n\n", "color": "white"}, ["", {"text": "Item", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "id", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"ruby\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "base_item", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"minecraft:diamond\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "components", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "{", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "\"lore\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "[{", "color": "#F8F8F2"}, {"text": "\"text\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "\"Shiny!\"", "color": "#F1FA8C"}, {"text": "}],", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "},", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": ")", "color": "#F8F8F2"}]]
data modify entity 20180612-2026-2002-2098-202000000003 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000003 transformation.scale set value [0.55f, 0.55f, 0.55f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000003 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000003 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000003 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000003 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000003 height set value 0.0f

