
#> stewbeet_summit:walls/recipes_loot/page_5
#
# @within	stewbeet_summit:walls/recipes_loot/show
#

# Page 6/6 "Loot & Manual, For Free": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000006 text set value ["", {"text": "The payoff (6/6)\n\n", "bold": true, "color": "gold"}, {"text": "Every item gets a ", "color": "white"}, {"text": "loot table", "bold": true, "color": "aqua"}, {"text": ", and a ", "color": "white"}, {"text": "_give_all", "bold": true, "color": "aqua"}, {"text": " function hands out chests of everything you made - great for tests.\n\nBetter yet: every recipe is ", "color": "white"}, {"text": "rendered", "bold": true, "color": "gold"}, {"text": " into the in-game manual, automatically.\n\n", "color": "white"}, {"text": "Define once. Appreciate the rest.\n\n", "color": "#7F8C99", "italic": true}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Definitions Setup", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}}]]
data modify entity 20180612-2026-2002-2098-202000000006 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000006 transformation.scale set value [0.475f, 0.475f, 0.475f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000006 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000006 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000006 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000006 height set value 0.75f

