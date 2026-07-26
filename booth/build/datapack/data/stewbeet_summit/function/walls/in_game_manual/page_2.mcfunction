
#> stewbeet_summit:walls/in_game_manual/page_2
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 3/8 "Phase Hooks": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Hook the build (3/8)\n\n", "bold": true, "color": "gold"}, {"text": "Default pages only exist ", "color": "white"}, {"text": "during", "bold": true, "color": "gold"}, {"text": " the build,\nso register a function at the right ", "color": "white"}, {"text": "Phase", "bold": true, "color": "aqua"}, {"text": ":\n\n", "color": "white"}, ["", {"text": "manual", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "get_manual", "color": "#50FA7B"}, {"text": "()", "color": "#F8F8F2"}, {"text": "\n\n"}], ["", {"text": "@"}, {"text": "manual.", "color": "#F8F8F2"}, {"text": "on", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "Phase", "color": "#8BE9FD"}, {"text": ".", "color": "#F8F8F2"}, {"text": "PREPARED", "color": "#8BE9FD"}, {"text": ")", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "def", "color": "#FF79C6"}, {"text": " "}, {"text": "tweak", "color": "#50FA7B"}, {"text": "(m:", "color": "#F8F8F2"}, {"text": " "}, {"text": "Manual", "color": "#8BE9FD"}, {"text": "):", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "page", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "m.", "color": "#F8F8F2"}, {"text": "get_page_for_item", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"steel_ingot\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "DISCOVERED, PREPARED, ORDERED,\nRENDERED, RESOLVED, BEFORE_EMIT.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 250
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.0f

