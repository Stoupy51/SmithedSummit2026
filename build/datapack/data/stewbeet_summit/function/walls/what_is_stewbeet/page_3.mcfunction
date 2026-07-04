
#> stewbeet_summit:walls/what_is_stewbeet/page_3
#
# @within	stewbeet_summit:walls/what_is_stewbeet/show
#

# Page 4/4 "The Result": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000000 text set value ["", {"text": "The result (4/4)\n\n", "bold": true, "color": "gold"}, {"text": "Focus on your ", "color": "white"}, {"text": "ideas", "bold": true, "color": "gold"}, {"text": ", not boilerplate.\n\n", "color": "white"}, {"text": "- Fewer files\n- Fewer bugs\n- Much faster iteration", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000000 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000000 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000000 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000000 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000000 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000000 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000000 height set value 0.0f

