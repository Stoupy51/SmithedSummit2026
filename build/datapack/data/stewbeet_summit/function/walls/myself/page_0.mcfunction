
#> stewbeet_summit:walls/myself/page_0
#
# @within	stewbeet_summit:walls/myself/show
#

# Page 1/3 "Who Am I?": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000014 text set value ["", {"text": "Better to introduce myself now than never.\n\n", "color": "#7F8C99", "italic": true}, {"text": "Hi, I'm Stoupy! (1/3)\n\n", "bold": true, "color": "gold"}, {"text": "Playing Minecraft since the ", "color": "white"}, {"text": "1.0", "bold": true, "color": "gold"}, {"text": " release month (November 2011), doing ", "color": "white"}, {"text": "command blocks", "bold": true, "color": "gold"}, {"text": " since they were added, and ", "color": "white"}, {"text": "datapacks", "bold": true, "color": "gold"}, {"text": " since 1.15: ", "color": "white"}, {"text": "7 years", "bold": true, "color": "aqua"}, {"text": " ago.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "github.com/Stoupy51", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51"}}]]
data modify entity 20180612-2026-2002-2098-202000000014 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000014 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000014 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000014 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000014 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000014 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000014 height set value 0.75f

