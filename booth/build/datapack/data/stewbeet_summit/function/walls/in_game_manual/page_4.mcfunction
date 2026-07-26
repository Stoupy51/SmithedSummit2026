
#> stewbeet_summit:walls/in_game_manual/page_4
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 5/8 "Texture Pages": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Bring your own art (5/8)\n\n", "bold": true, "color": "gold"}, {"text": "Back a page with a ", "color": "white"}, {"text": "texture", "bold": true, "color": "aqua"}, {"text": ", text baked into the image itself:\n\n", "color": "white"}, ["", {"text": "manual.", "color": "#F8F8F2"}, {"text": "insert_page", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "TexturePage", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "anchor", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"tutorial\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "title", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"Tutorial\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "background", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"assets/tutorial_bg.png\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "baked_texts", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "[", "color": "#F8F8F2"}, {"text": "BakedText", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "text", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"Step 1: mine ore\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "xy", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "(", "color": "#F8F8F2"}, {"text": "20", "color": "#BD93F9"}, {"text": ",", "color": "#F8F8F2"}, {"text": " "}, {"text": "40", "color": "#BD93F9"}, {"text": "),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": ")],", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "),", "color": "#F8F8F2"}, {"text": " "}, {"text": "before", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"category:Materials\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}]]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.0f

