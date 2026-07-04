
#> stewbeet_summit:walls/material_sets/page_8
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 9/9 "Mix Anything": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Custom or vanilla (9/9)\n\n", "bold": true, "color": "gold"}, {"text": "One dict can hold many materials at once, even vanilla ones:\n\n", "color": "white"}, ["", {"text": "\"steel_ingot\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "EquipmentsConfig", "color": "#8BE9FD"}, {"text": "(...),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "\"minecraft:emerald\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "EquipmentsConfig", "color": "#8BE9FD"}, {"text": "(...),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "\"minecraft:stone\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "None", "color": "#FF79C6"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "Pass ", "color": "white"}, {"text": "None", "bold": true, "color": "aqua"}, {"text": " for no stats: stone still finds your ", "color": "white"}, {"text": "stone_stick", "bold": true, "color": "aqua"}, {"text": " and ", "color": "white"}, {"text": "stone_rod", "bold": true, "color": "aqua"}, {"text": " textures on its own.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Definitions Setup", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}}]]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.75f

