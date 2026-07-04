
#> stewbeet_summit:walls/standing_on_giants/page_6
#
# @within	stewbeet_summit:walls/standing_on_giants/show
#

# Page 7/7 "More Libraries": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000005 text set value ["", {"text": "...and more libraries (7/7)\n\n", "bold": true, "color": "gold"}, {"text": "Each pulled in automatically only when a function references it:\n\n", "color": "white"}, {"text": "Furnace NBT Recipes", "bold": true, "color": "aqua"}, {"text": " - furnaces\n", "color": "white"}, {"text": "Common Signals", "bold": true, "color": "aqua"}, {"text": " - event hooks\n", "color": "white"}, {"text": "ItemIO", "bold": true, "color": "aqua"}, {"text": " - item transport\n", "color": "white"}, {"text": "Realistic Explosion", "bold": true, "color": "aqua"}, {"text": " - blasts\n", "color": "white"}, {"text": "Smithed Actionbar", "bold": true, "color": "aqua"}, {"text": " - action bar\n", "color": "white"}, {"text": "Player Motion", "bold": true, "color": "aqua"}, {"text": " - movement\n", "color": "white"}, {"text": "...and more!\n\n", "color": "#7F8C99", "italic": true}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Libraries Support", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=5_dependencies%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=5_dependencies%2Fen.md"}}]]
data modify entity 20180612-2026-2002-2098-202000000005 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000005 transformation.scale set value [0.475f, 0.475f, 0.475f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000005 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000005 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000005 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000005 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000005 height set value 0.75f

