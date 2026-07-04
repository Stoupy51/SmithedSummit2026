
#> stewbeet_summit:walls/in_game_manual/page_5
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 6/8 "Button Layout": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Buttons, your way (6/8)\n\n", "bold": true, "color": "gold"}, {"text": "Decide where wiki buttons go and how overflow is handled:\n\n", "color": "white"}, ["", {"text": "page.button_layout", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "ButtonLayout", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "columns", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "6", "color": "#BD93F9"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "max_buttons", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "42", "color": "#BD93F9"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "position", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"after_recipe\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "order", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "(", "color": "#F8F8F2"}, {"text": "lambda", "color": "#FF79C6"}, {"text": " "}, {"text": "b:", "color": "#F8F8F2"}, {"text": " "}, {"text": "-", "color": "#FF79C6"}, {"text": "b.priority),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": ")", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "Per page, or as the manual-wide default.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.0f

