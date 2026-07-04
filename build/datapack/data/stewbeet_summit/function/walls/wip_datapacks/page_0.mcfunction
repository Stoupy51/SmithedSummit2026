
#> stewbeet_summit:walls/wip_datapacks/page_0
#
# @within	stewbeet_summit:walls/wip_datapacks/show
#

# Page 1/6 "MC Guns System": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000013 text set value ["", {"text": "MC Guns System (1/6)\n\n", "bold": true, "color": "gold"}, {"text": "A full ", "color": "white"}, {"text": "FPS framework", "bold": true, "color": "gold"}, {"text": " for Minecraft: a complete rewrite of MGS 4.2, built with ", "color": "white"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": ".\n\n", "color": "white"}, {"text": "Weapons are ", "color": "white"}, {"text": "data-driven", "bold": true, "color": "aqua"}, {"text": ": all the stats live on the items, not in hardcoded logic.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "github.com/Stoupy51/MC_Guns_System", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/MC_Guns_System"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/MC_Guns_System"}}]]
data modify entity 20180612-2026-2002-2098-202000000013 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000013 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000013 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000013 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000013 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000013 height set value 0.75f

