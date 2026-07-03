
#> stewbeet_summit:walls/in_game_manual/page_2
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "Never stale (3/3)\n\n", "bold": true, "color": "gold"}, {"text": "Add an item, rebuild, and the manual updates ", "color": "white"}, {"text": "itself", "bold": true, "color": "gold"}, {"text": ".\n\n", "color": "white"}, {"text": "Book or in-game dialog UI.\n\n", "color": "#7F8C99", "italic": true}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: In-Game Manual", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md"}}]]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.6f, 0.6f, 0.6f]
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.75f

