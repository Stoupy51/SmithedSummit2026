
#> stewbeet_summit:walls/qol_ecosystem/page_5
#
# @within	stewbeet_summit:walls/qol_ecosystem/show
#

# Page 6/6 "Thank You": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000009 text set value ["", {"text": "Thank you! (6/6)\n\n", "bold": true, "color": "gold"}, {"text": "Build more. Write less.\n\nPowered by ", "color": "white"}, {"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}, {"text": ".\n\n", "color": "white"}, {"text": "Curious about how this booth was made? Check the source code at\n", "color": "#7F8C99", "italic": true}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "github.com/Stoupy51/SmithedSummit2026", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/SmithedSummit2026"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/SmithedSummit2026"}}]]
data modify entity 20180612-2026-2002-2098-202000000009 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000009 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000009 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000009 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000009 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000009 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000009 height set value 0.75f

