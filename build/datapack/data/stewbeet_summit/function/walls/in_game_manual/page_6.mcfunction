
#> stewbeet_summit:walls/in_game_manual/page_6
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 7/8 "Custom Recipe Types": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Render new crafts (7/8)\n\n", "bold": true, "color": "gold"}, {"text": "One class + one call teaches the manual a whole new recipe type. The real ", "color": "white"}, {"text": "Pulverizer", "bold": true, "color": "aqua"}, {"text": " support:\n\n", "color": "white"}, ["", {"text": "class", "color": "#FF79C6"}, {"text": " "}, {"text": "PulverizingRenderer", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "LinearRenderer", "color": "#8BE9FD"}, {"text": "):", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "types", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "(", "color": "#F8F8F2"}, {"text": "PulverizingRecipe", "color": "#8BE9FD"}, {"text": ".type,)", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "name", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "\"(SimplEnergy) Pulverizing\"", "color": "#F1FA8C"}, {"text": "\n\n"}], ["", {"text": "    "}, {"text": "def", "color": "#FF79C6"}, {"text": " "}, {"text": "static_glyph", "color": "#50FA7B"}, {"text": "(self,", "color": "#F8F8F2"}, {"text": " "}, {"text": "craft):", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "return", "color": "#FF79C6"}, {"text": " "}, {"text": "PULVERIZING_FONT", "color": "#8BE9FD"}, {"text": "\n\n"}], ["", {"text": "register_craft_renderer", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "PulverizingRenderer", "color": "#8BE9FD"}, {"text": "())", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "LinearRenderer draws the shared\n\"ingredient -> result\" row layout.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 250
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.42f, 0.42f, 0.42f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.0f

