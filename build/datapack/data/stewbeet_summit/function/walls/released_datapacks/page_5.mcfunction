
#> stewbeet_summit:walls/released_datapacks/page_5
#
# @within	stewbeet_summit:walls/released_datapacks/show
#

# Page 6/6 "And More": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000012 text set value ["", {"text": "...and more! (6/6)\n\n", "bold": true, "color": "gold"}, {"text": "Check my profiles for the full collection:\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "planetminecraft.com/member/stoupy", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://www.planetminecraft.com/member/stoupy/"}, "hover_event": {"action": "show_text", "value": "Open https://www.planetminecraft.com/member/stoupy/"}}], {"text": "\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.modrinth"}, {"text": " "}, {"text": "modrinth.com/user/Stoupy51", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://modrinth.com/user/Stoupy51"}, "hover_event": {"action": "show_text", "value": "Open https://modrinth.com/user/Stoupy51"}}], {"text": "\n\n", "color": "white"}, {"text": "100% of them powered by StewBeet.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000012 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000012 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000012 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000012 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+1)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000012 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000012 height set value 0.75f

