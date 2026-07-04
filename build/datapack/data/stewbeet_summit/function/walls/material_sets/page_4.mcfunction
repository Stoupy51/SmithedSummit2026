
#> stewbeet_summit:walls/material_sets/page_4
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 5/9 "Wears On Your Body": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Armor that renders (5/9)\n\n", "bold": true, "color": "gold"}, {"text": "Add two layer textures beside the gear:\n\n", "color": "white"}, ["", {"text": "steel_layer_1.png", "color": "#F8F8F2"}, {"text": "  "}, {"text": "# body & head", "color": "#6272A4"}, {"text": "\n"}], ["", {"text": "steel_layer_2.png", "color": "#F8F8F2"}, {"text": "  "}, {"text": "# legs & feet", "color": "#6272A4"}, {"text": "\n\n"}], [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": " copies them into the assets/*/equipment folder and wires the ", "color": "white"}, {"text": "equippable", "bold": true, "color": "aqua"}, {"text": " component - so your set actually shows ", "color": "white"}, {"text": "on the player", "bold": true, "color": "gold"}, {"text": ", not just in the slot.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

