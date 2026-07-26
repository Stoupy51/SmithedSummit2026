
#> stewbeet_summit:walls/items_in_pure_python/page_4
#
# @within	stewbeet_summit:walls/items_in_pure_python/show
#

# Page 5/5 "Access Anywhere": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000003 text set value ["", {"text": "One global registry (5/5)\n\n", "bold": true, "color": "gold"}, {"text": "Every definition lives in ", "color": "white"}, {"text": "Mem.definitions", "bold": true, "color": "aqua"}, {"text": ". You can access it from anywhere and update it.\n\n", "color": "white"}, ["", {"text": "ruby", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "Item", "color": "#8BE9FD"}, {"text": ".", "color": "#F8F8F2"}, {"text": "from_id", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"ruby\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "ruby.manual_category", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "\"materials\"", "color": "#F1FA8C"}, {"text": "\n\n"}], ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Definitions Setup", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}}]]
data modify entity 20180612-2026-2002-2098-202000000003 line_width set value 200
data modify entity 20180612-2026-2002-2098-202000000003 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000003 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000003 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000003 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000003 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000003 height set value 0.75f

