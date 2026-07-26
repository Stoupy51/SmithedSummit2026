
#> stewbeet_summit:walls/qol_ecosystem/page_3
#
# @within	stewbeet_summit:walls/qol_ecosystem/show
#

# Page 4/6 "Compatibilities": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000009 text set value ["", {"text": "Plays well with others (4/6)\n\n", "bold": true, "color": "gold"}, {"text": "Automatic special support for:", "color": "white"}, {"text": "\n\n- SimpleDrawer compacted drawers\n ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[compatibilities.simpledrawer]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/compatibilities.simpledrawer.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/compatibilities.simpledrawer.md"}}], {"text": "\n\n- NeoEnchant veinminer\n ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[compatibilities.neo_enchant]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/compatibilities.neo_enchant.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/compatibilities.neo_enchant.md"}}], {"text": "\n\n- SimplEnergy pulverizer\n ", "color": "white"}, ["", {"text": "[PulverizingRecipe]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stoupy51.github.io/StewBeet/latest/modules/stewbeet.core.cls.recipe.html#stewbeet.core.cls.recipe.PulverizingRecipe"}, "hover_event": {"action": "show_text", "value": "Open https://stoupy51.github.io/StewBeet/latest/modules/stewbeet.core.cls.recipe.html#stewbeet.core.cls.recipe.PulverizingRecipe"}}]]
data modify entity 20180612-2026-2002-2098-202000000009 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000009 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000009 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000009 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000009 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+2)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000009 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000009 height set value 0.75f

