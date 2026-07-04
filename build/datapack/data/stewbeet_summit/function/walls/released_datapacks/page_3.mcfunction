
#> stewbeet_summit:walls/released_datapacks/page_3
#
# @within	stewbeet_summit:walls/released_datapacks/show
#

# Page 4/6 "Random Mob Sizes": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000012 text set value ["", {"text": "Random Mob Sizes (4/6)\n\n", "bold": true, "color": "gold"}, {"text": "Every mob spawns at a random ", "color": "white"}, {"text": "scale", "bold": true, "color": "aqua"}, {"text": " for varied encounters.\n\n", "color": "white"}, {"text": "Optionally ties ", "color": "white"}, {"text": "health", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "speed", "bold": true, "color": "aqua"}, {"text": " and ", "color": "white"}, {"text": "damage", "bold": true, "color": "aqua"}, {"text": " to the size, with per-mob overrides and an in-game config.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "[PMC]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://www.planetminecraft.com/data-pack/random-mob-sizes-6264344/"}, "hover_event": {"action": "show_text", "value": "Open https://www.planetminecraft.com/data-pack/random-mob-sizes-6264344/"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.modrinth"}, {"text": " "}, {"text": "[Modrinth]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://modrinth.com/datapack/random-mob-sizes-dp"}, "hover_event": {"action": "show_text", "value": "Open https://modrinth.com/datapack/random-mob-sizes-dp"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[GitHub]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/RandomMobSizes/releases/latest"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/RandomMobSizes/releases/latest"}}]]
data modify entity 20180612-2026-2002-2098-202000000012 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000012 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000012 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000012 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000012 height set value 0.75f

