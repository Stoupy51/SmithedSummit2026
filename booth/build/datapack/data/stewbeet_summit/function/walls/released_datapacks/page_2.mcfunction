
#> stewbeet_summit:walls/released_datapacks/page_2
#
# @within	stewbeet_summit:walls/released_datapacks/show
#

# Page 3/6 "Stardust Fragment": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000012 text set value ["", {"text": "Stardust Fragment (3/6)\n\n", "bold": true, "color": "gold"}, {"text": "A whole tech-adventure progression:\n\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "190+", "bold": true, "color": "aqua"}, {"text": " items across 6 tiers\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "35+", "bold": true, "color": "aqua"}, {"text": " energy devices\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "5", "bold": true, "color": "aqua"}, {"text": " custom dimensions\n", "color": "white"}, {"text": "- mini-bosses & end-game bosses\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "100+", "bold": true, "color": "aqua"}, {"text": " advancements & manual pages\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "[PMC]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://www.planetminecraft.com/data-pack/stardust-fragment/"}, "hover_event": {"action": "show_text", "value": "Open https://www.planetminecraft.com/data-pack/stardust-fragment/"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.modrinth"}, {"text": " "}, {"text": "[Modrinth]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://modrinth.com/datapack/stardust-fragment"}, "hover_event": {"action": "show_text", "value": "Open https://modrinth.com/datapack/stardust-fragment"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[GitHub]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/StardustFragment"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/StardustFragment"}}]]
data modify entity 20180612-2026-2002-2098-202000000012 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000012 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000012 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000012 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000012 height set value 0.75f

