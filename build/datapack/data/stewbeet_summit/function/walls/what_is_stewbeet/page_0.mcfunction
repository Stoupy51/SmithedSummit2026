
#> stewbeet_summit:walls/what_is_stewbeet/page_0
#
# @within	stewbeet_summit:walls/what_is_stewbeet/show
#

# Page 1/4 "Introduction": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000000 text set value ["", {"text": "Introduction (1/4)\n\n", "bold": true, "color": "gold"}, {"text": "It is a ", "color": "white"}, [{"text": "B", "color": "#00c400", "italic": false}, {"text": "e", "color": "#558200"}, {"text": "e", "color": "#aa4100"}, {"text": "t", "color": "#ff0000"}], {"text": " framework that brings huge ", "color": "white"}, {"text": "automation", "bold": true, "color": "aqua"}, {"text": " to Minecraft datapacks.\n\n", "color": "white"}, {"text": "You describe ", "color": "white"}, {"text": "what", "bold": true, "color": "gold"}, {"text": " you want in Python. ", "color": "white"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": " generates everything else.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "stewbeet.paralya.fr", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr"}}], {"text": "\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.discord"}, {"text": " "}, {"text": "discord.gg/anxzu6rA9F", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://discord.gg/anxzu6rA9F"}, "hover_event": {"action": "show_text", "value": "Open https://discord.gg/anxzu6rA9F"}}], {"text": "\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Made by Stoupy", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/StewBeet"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/StewBeet"}}]]
data modify entity 20180612-2026-2002-2098-202000000000 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000000 transformation.scale set value [0.55f, 0.55f, 0.55f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000000 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000000 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000000 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000000 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000000 height set value 0.75f

