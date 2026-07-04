
#> stewbeet_summit:walls/material_sets/page_0
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 1/9 "One Config": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Describe it once (1/9)\n\n", "bold": true, "color": "gold"}, {"text": "A new metal usually means dozens of items, models and recipes, all by hand.\n\nWith ", "color": "white"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": ", you write ", "color": "white"}, {"text": "one", "bold": true, "color": "aqua"}, {"text": " code block:\n\n", "color": "white"}, ["", {"text": "ORES_CONFIGS", "color": "#8BE9FD"}, {"text": " "}, {"text": "=", "color": "#FF79C6"}, {"text": " "}, {"text": "{", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "\"steel_ingot\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "EquipmentsConfig", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "equivalent_to", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "DefaultOre", "color": "#8BE9FD"}, {"text": ".", "color": "#F8F8F2"}, {"text": "IRON", "color": "#8BE9FD"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "}", "color": "#F8F8F2"}]]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

