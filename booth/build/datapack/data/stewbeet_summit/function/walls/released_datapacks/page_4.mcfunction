
#> stewbeet_summit:walls/released_datapacks/page_4
#
# @within	stewbeet_summit:walls/released_datapacks/show
#

# Page 5/6 "My Libraries": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000012 text set value ["", {"text": "My libraries (5/6)\n\n", "bold": true, "color": "gold"}, {"text": "Shared building blocks,\nfree to use in your own packs:\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[Realistic Explosion]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/RealisticExplosion"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/RealisticExplosion"}}], {"text": " optimized realistic blasts\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[Furnace NBT Recipes]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/FurnaceNbtRecipes"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/FurnaceNbtRecipes"}}], {"text": " custom furnace recipes\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[Smart Ore Generation]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/SmartOreGeneration"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/SmartOreGeneration"}}], {"text": " custom ore veins\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[Common Signals]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/CommonSignals"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/CommonSignals"}}], {"text": " shared selectors & hooks", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000012 line_width set value 275
data modify entity 20180612-2026-2002-2098-202000000012 transformation.scale set value [0.55f, 0.55f, 0.55f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000012 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000012 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+3)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000012 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000012 height set value 0.75f

