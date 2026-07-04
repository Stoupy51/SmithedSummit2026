
#> stewbeet_summit:walls/in_game_manual/page_1
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 2/8 "Wiki Buttons": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Add your own notes (2/8)\n\n", "bold": true, "color": "gold"}, {"text": "Give an item ", "color": "white"}, {"text": "wiki_buttons", "bold": true, "color": "aqua"}, {"text": " and each one shows up as a hoverable button on its page:\n\n", "color": "white"}, ["", {"text": "Item", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "id", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"steel_ingot\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "wiki_buttons", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "[", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "WikiButton", "color": "#8BE9FD"}, {"text": "({", "color": "#F8F8F2"}, {"text": "\"text\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "\"Any text component here.\"", "color": "#F1FA8C"}, {"text": "}),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "WikiButton", "color": "#8BE9FD"}, {"text": "({", "color": "#F8F8F2"}, {"text": "\"text\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "\"Another one!\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": " "}, {"text": "\"color\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "\"aqua\"", "color": "#F1FA8C"}, {"text": "}),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "],", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": ")", "color": "#F8F8F2"}]]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 250
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.0f

