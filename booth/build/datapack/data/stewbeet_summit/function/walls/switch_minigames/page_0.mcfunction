
#> stewbeet_summit:walls/switch_minigames/page_0
#
# @within	stewbeet_summit:walls/switch_minigames/show
#

# Page 1/3 "Switch Minigames": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000011 text set value ["", {"text": "Switch Minigames (1/3)\n\n", "bold": true, "color": "gold"}, {"text": "A ", "color": "white"}, {"text": "democratic", "bold": true, "color": "gold"}, {"text": " minigame server, always on the latest Minecraft version. Still in beta, soon to be released as a public server.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.discord"}, {"text": " "}, {"text": "Be notified of updates", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://discord.gg/anxzu6rA9F"}, "hover_event": {"action": "show_text", "value": "Open https://discord.gg/anxzu6rA9F"}}], {"text": "\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Terrifying source code", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Paralya/Switch"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Paralya/Switch"}}]]
data modify entity 20180612-2026-2002-2098-202000000011 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000011 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000011 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000011 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000011 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.discord"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+1)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000011 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000011 height set value 0.75f

