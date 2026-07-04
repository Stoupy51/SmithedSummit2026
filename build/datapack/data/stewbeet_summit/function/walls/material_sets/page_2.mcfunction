
#> stewbeet_summit:walls/material_sets/page_2
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 3/9 "Textures Lead": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Your art decides (3/9)\n\n", "bold": true, "color": "gold"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": " scans your textures folder and builds ", "color": "white"}, {"text": "only", "bold": true, "color": "aqua"}, {"text": " what it finds there.\n\n", "color": "white"}, {"text": "Drop in a ", "color": "white"}, {"text": "steel_sword.png", "color": "#8BE9FD"}, {"text": " and a steel sword exists. No file, no item.\n\n", "color": "white"}, {"text": "Add the art, rebuild, it's there.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

