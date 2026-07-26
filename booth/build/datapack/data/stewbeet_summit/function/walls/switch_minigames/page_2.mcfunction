
#> stewbeet_summit:walls/switch_minigames/page_2
#
# @within	stewbeet_summit:walls/switch_minigames/show
#

# Page 3/3 "The Minigames": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000011 text set value ["", {"text": "50+ minigames (3/3)\n\n", "bold": true, "color": "gold"}, {"text": "The initial goal was 48... we now aim for an ", "color": "white"}, {"text": "infinite", "bold": true, "color": "gold"}, {"text": " number!\n\n", "color": "white"}, {"text": "Spend the server's ", "color": "white"}, {"text": "Sapphire", "bold": true, "color": "aqua"}, {"text": " currency on cosmetic advantages in certain games.\n\n", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.youtube"}, {"text": " "}, {"text": "2 years of memories (video)", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://www.youtube.com/watch?v=cB27sEOxboA"}, "hover_event": {"action": "show_text", "value": "Open https://www.youtube.com/watch?v=cB27sEOxboA"}}]]
data modify entity 20180612-2026-2002-2098-202000000011 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000011 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000011 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000011 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000011 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.youtube"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}]
data modify entity 20180612-2026-2002-2098-202400000011 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000011 height set value 0.75f

