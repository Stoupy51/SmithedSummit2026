
#> stewbeet_summit:walls/recipes_loot/page_3
#
# @within	stewbeet_summit:walls/recipes_loot/show
#

# Page 4/6 "One Ingredient Helper": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000006 text set value ["", {"text": "Ingr, any source (4/6)\n\n", "bold": true, "color": "gold"}, ["", {"text": "Ingr", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"minecraft:stick\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}, {"text": " "}, {"text": "# vanilla", "color": "#6272A4"}, {"text": "\n"}], ["", {"text": "Ingr", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"ruby\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}, {"text": "             "}, {"text": "# your pack", "color": "#6272A4"}, {"text": "\n"}], ["", {"text": "Ingr", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"tin\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": " "}, {"text": "ns", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"mech\"", "color": "#F1FA8C"}, {"text": ")", "color": "#F8F8F2"}, {"text": "  "}, {"text": "# other pack", "color": "#6272A4"}, {"text": "\n\n"}], {"text": "The same ", "color": "white"}, {"text": "Ingr", "bold": true, "color": "aqua"}, {"text": " everywhere, it works out the item data and NBT for you. ", "color": "white"}, {"text": "You can also use ", "color": "white"}, {"text": "Ingredient", "bold": true, "color": "aqua"}, {"text": " as an alias.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000006 line_width set value 200
data modify entity 20180612-2026-2002-2098-202000000006 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000006 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000006 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000006 height set value 0.0f

