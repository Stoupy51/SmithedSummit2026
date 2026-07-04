
#> stewbeet_summit:walls/why_for_who/page_0
#
# @within	stewbeet_summit:walls/why_for_who/show
#

# Page 1/4 "Modular": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000001 text set value ["", {"text": "Modular by design (1/4)\n\n", "bold": true, "color": "gold"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": " is a ", "color": "white"}, {"text": "pipeline", "bold": true, "color": "aqua"}, {"text": " of plugins.\n\n", "color": "white"}, {"text": "Use the full suite for complete generation, or pick ", "color": "white"}, {"text": "only", "bold": true, "color": "gold"}, {"text": " the features you actually need.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000001 line_width set value 175
data modify entity 20180612-2026-2002-2098-202000000001 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000001 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000001 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

