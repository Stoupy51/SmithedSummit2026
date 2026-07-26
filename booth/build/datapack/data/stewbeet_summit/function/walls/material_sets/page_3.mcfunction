
#> stewbeet_summit:walls/material_sets/page_3
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 4/9 "Recipes Included": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Crafts, for free (4/9)\n\n", "bold": true, "color": "gold"}, {"text": "Every generated item is already wired up:\n\n- Raw & dust ", "color": "white"}, {"text": "smelt", "bold": true, "color": "aqua"}, {"text": " to the ingot\n- Shapeless: 9 ingots ", "color": "white"}, {"text": "<->", "bold": true, "color": "aqua"}, {"text": " 1 block\n- Shapeless: 9 nuggets ", "color": "white"}, {"text": "<->", "bold": true, "color": "aqua"}, {"text": " 1 ingot\n", "color": "white"}, {"text": "- Tools & armor get their crafting ", "color": "white"}, {"text": "shapes", "bold": true, "color": "aqua"}, {"text": "\n- Melt old gear back into ", "color": "white"}, {"text": "nuggets", "bold": true, "color": "aqua"}, {"text": "\n- The ore ", "color": "white"}, {"text": "drops", "bold": true, "color": "aqua"}, {"text": " when no silk touch\n- ...\n\n", "color": "white"}, {"text": "Blasting + pulverizing (2x dust) too.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

