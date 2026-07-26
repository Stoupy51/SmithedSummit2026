
#> stewbeet_summit:walls/in_game_manual/page_3
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 4/8 "Custom Pages": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Insert any page (4/8)\n\n", "bold": true, "color": "gold"}, {"text": "Slot a ", "color": "white"}, {"text": "CustomPage", "bold": true, "color": "aqua"}, {"text": " anywhere, even unrelated to items:\n\n", "color": "white"}, ["", {"text": "manual.", "color": "#F8F8F2"}, {"text": "insert_page", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "CustomPage", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "anchor", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"welcome\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "title", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"Welcome\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "body", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "[{", "color": "#F8F8F2"}, {"text": "\"text\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "\"Hello!\"", "color": "#F1FA8C"}, {"text": "}],", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "),", "color": "#F8F8F2"}, {"text": " "}, {"text": "after", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"intro\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "Links are deferred (", "color": "white"}, {"text": "PageRef", "bold": true, "color": "aqua"}, {"text": "): insert or reorder pages, navigation never breaks.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.0f

