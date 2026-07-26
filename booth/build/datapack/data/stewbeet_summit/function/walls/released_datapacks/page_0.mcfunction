
#> stewbeet_summit:walls/released_datapacks/page_0
#
# @within	stewbeet_summit:walls/released_datapacks/show
#

# Page 1/6 "LifeSteal FR": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000012 text set value ["", {"text": "LifeSteal FR (1/6)\n\n", "bold": true, "color": "gold"}, {"text": "The Lifesteal SMP experience:\nkill a player, ", "color": "white"}, {"text": "steal a heart", "bold": true, "color": "red"}, {"text": ".\n\n", "color": "white"}, {"text": "Craft hearts, revive the fallen with ", "color": "white"}, {"text": "revive beacons", "bold": true, "color": "aqua"}, {"text": ", and tune every rule from an in-game ", "color": "white"}, {"text": "config", "bold": true, "color": "aqua"}, {"text": " menu.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "[PMC]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://www.planetminecraft.com/data-pack/life-steal-fr/"}, "hover_event": {"action": "show_text", "value": "Open https://www.planetminecraft.com/data-pack/life-steal-fr/"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.modrinth"}, {"text": " "}, {"text": "[Modrinth]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://modrinth.com/datapack/lifestealfr"}, "hover_event": {"action": "show_text", "value": "Open https://modrinth.com/datapack/lifestealfr"}}], {"text": " ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[GitHub]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/LifeSteal"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/LifeSteal"}}]]
data modify entity 20180612-2026-2002-2098-202000000012 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000012 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000012 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000012 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.planetminecraft"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000012 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000012 height set value 0.75f

