
#> stewbeet_summit:walls/material_sets/page_5
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 6/9 "Give It A Personality": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Not just a reskin (6/9)\n\n", "bold": true, "color": "gold"}, {"text": "Make your config relative to a vanilla tier, and bend the numbers:\n\n", "color": "white"}, ["", {"text": "equivalent_to", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "DefaultOre", "color": "#8BE9FD"}, {"text": ".", "color": "#F8F8F2"}, {"text": "IRON", "color": "#8BE9FD"}, {"text": "\n"}], ["", {"text": "pickaxe_durability", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "3", "color": "#BD93F9"}, {"text": " "}, {"text": "*", "color": "#FF79C6"}, {"text": " "}, {"text": "iron", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "attributes", "color": "#F8F8F2"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "{", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "\"attack_damage\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "1", "color": "#BD93F9"}, {"text": ",", "color": "#F8F8F2"}, {"text": "      "}, {"text": "# +1 a hit", "color": "#6272A4"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "\"mining_efficiency\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "2", "color": "#BD93F9"}, {"text": ",", "color": "#F8F8F2"}, {"text": "   "}, {"text": "# +20% speed", "color": "#6272A4"}, {"text": "\n"}], ["", {"text": "}", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "Steel: iron's stats, but the whole set is ", "color": "white"}, {"text": "3x tougher", "bold": true, "color": "aqua"}, {"text": " and quicker to mine with.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

