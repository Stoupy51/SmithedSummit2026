
#> stewbeet_summit:walls/in_game_manual/page_0
#
# @within	stewbeet_summit:walls/in_game_manual/show
#

# Page 1/8 "Free Documentation": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000008 text set value ["", {"text": "A manual, generated (1/8)\n\n", "bold": true, "color": "gold"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": " builds a full ", "color": "white"}, {"text": "interactive", "bold": true, "color": "aqua"}, {"text": " manual from your items and recipes.\n\n", "color": "white"}, {"text": "Every recipe, rendered and clickable.\n\n", "color": "#7F8C99", "italic": true}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Please check the GIF!\nI highly recommend it!!!", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://github.com/Stoupy51/StewBeet/blob/main/docs/plugins/img/ingame_manual.gif"}, "hover_event": {"action": "show_text", "value": "Open https://github.com/Stoupy51/StewBeet/blob/main/docs/plugins/img/ingame_manual.gif"}}]]
data modify entity 20180612-2026-2002-2098-202000000008 line_width set value 195
data modify entity 20180612-2026-2002-2098-202000000008 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000008 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000008 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000008 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000008 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000008 height set value 0.75f

