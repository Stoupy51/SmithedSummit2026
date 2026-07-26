
#> stewbeet_summit:walls/material_sets/page_1
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 2/9 "The Whole Family": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "One line in, a set out (2/9)\n\n", "bold": true, "color": "gold"}, ["", {"text": "generate_everything_about_these_materials", "color": "#50FA7B"}, {"text": "(", "color": "#F8F8F2"}, {"text": "ORES_CONFIGS", "color": "#8BE9FD"}, {"text": ")", "color": "#F8F8F2"}, {"text": "\n\n"}], {"text": "And out comes the whole family:\n\n", "color": "white"}, {"text": "steel_ingot, steel_nugget, raw_steel, steel_dust, steel_block, steel_ore, deepslate_steel_ore, ", "color": "#538b97"}, {"text": "steel_pickaxe, steel_axe, steel_sword, steel_shovel, steel_hoe, steel_spear, ", "color": "#70becf"}, {"text": "steel_helmet, steel_chestplate, steel_leggings, steel_boots, and more...\n\n", "color": "#538b97"}, {"text": "Around 20 items, from one config.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 225
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.42f, 0.42f, 0.42f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

