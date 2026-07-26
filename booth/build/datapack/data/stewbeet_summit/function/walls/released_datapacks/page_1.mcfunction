
#> stewbeet_summit:walls/released_datapacks/page_1
#
# @within	stewbeet_summit:walls/released_datapacks/show
#

# Page 2/6 "SimplEnergy": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000012 text set value ["", {"text": "SimplEnergy (2/6)\n\n", "bold": true, "color": "gold"}, {"text": "Simple ", "color": "white"}, {"text": "energy", "bold": true, "color": "gold"}, {"text": " for survival: solar panels, 3 battery tiers, energy and item cables, electric furnaces, pulverizers...\n\n", "color": "white"}, {"text": "Also a clean ", "color": "white"}, {"text": "template", "bold": true, "color": "aqua"}, {"text": " for building your own energy datapack with ", "color": "white"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": ".\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "[PMC]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://www.planetminecraft.com/data-pack/simplenergy/"}, "hover_event": {"action": "show_text", "value": "Open https://www.planetminecraft.com/data-pack/simplenergy/"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.modrinth"}, {"text": " "}, {"text": "[Modrinth]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://modrinth.com/datapack/simplenergy"}, "hover_event": {"action": "show_text", "value": "Open https://modrinth.com/datapack/simplenergy"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[GitHub]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/SimplEnergy"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/SimplEnergy"}}]]
data modify entity 20180612-2026-2002-2098-202000000012 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000012 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000012 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000012 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000012 height set value 0.75f

