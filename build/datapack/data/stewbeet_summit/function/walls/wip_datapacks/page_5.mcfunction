
#> stewbeet_summit:walls/wip_datapacks/page_5
#
# @within	stewbeet_summit:walls/wip_datapacks/show
#

# Page 6/6 "ImagineYourCraft": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000013 text set value ["", {"text": "ImagineYourCraft (6/6)\n", "bold": true, "color": "gold"}, {"text": "Totally unrelated to MGS.\n\n", "color": "#7F8C99", "italic": true}, {"text": "Recreating an old modded server's mod as a pure ", "color": "white"}, {"text": "datapack", "bold": true, "color": "gold"}, {"text": ".\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "github.com/Stoupy51/ImagineYourCraftDatapack", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/ImagineYourCraftDatapack"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/ImagineYourCraftDatapack"}}]]
data modify entity 20180612-2026-2002-2098-202000000013 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000013 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000013 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000013 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000013 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000013 height set value 0.75f

