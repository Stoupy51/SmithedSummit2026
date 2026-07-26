
#> stewbeet_summit:walls/in_game_manual/page_7
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 8/8 "Always Up To Date": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Never stale (8/8)\n\n", "bold": true, "color": "gold"}, {"text": "Add an item, rebuild, and the manual updates ", "color": "white"}, {"text": "itself", "bold": true, "color": "gold"}, {"text": ".\n\n", "color": "white"}, {"text": "Dialog UI, can be opened from the vanilla quick actions menu.\n\n", "color": "#7F8C99", "italic": true}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: In-Game Manual", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md"}}]]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.75f

