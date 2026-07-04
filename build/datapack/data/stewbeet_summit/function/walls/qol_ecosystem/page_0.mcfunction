
#> stewbeet_summit:walls/qol_ecosystem/page_0
#
# @within	stewbeet_summit:walls/qol_ecosystem/show
#

# Page 1/6 "Auto Everything": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000009 text set value ["", {"text": "It writes the chores (1/6)\n\n", "bold": true, "color": "gold"}, {"text": "- ", "color": "white"}, {"text": "en_us.json", "bold": true, "color": "aqua"}, {"text": " lang file\n ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[auto.lang_file]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/auto.lang_file.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/auto.lang_file.md"}}], {"text": "\n\n- Function ", "color": "white"}, {"text": "headers\n ", "bold": true, "color": "aqua"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[auto.headers]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/auto.headers.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/auto.headers.md"}}], {"text": "\n\n- Scoreboard ", "color": "white"}, {"text": "constants", "bold": true, "color": "aqua"}, {"text": " detection\n ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[auto.scoreboard_constants]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/auto.scoreboard_constants.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/auto.scoreboard_constants.md"}}], {"text": "\n\nDetected from your code, automatically.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000009 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000009 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000009 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000009 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000009 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000009 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000009 height set value 0.75f

