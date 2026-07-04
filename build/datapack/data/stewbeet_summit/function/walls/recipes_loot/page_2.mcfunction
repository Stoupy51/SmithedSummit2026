
#> stewbeet_summit:walls/recipes_loot/page_2
#
# @within	stewbeet_summit:walls/recipes_loot/show
#

# Page 3/6 "Custom Items Craft Anyway": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000006 text set value ["", {"text": "The clever part (3/6)\n\n", "bold": true, "color": "gold"}, {"text": "Vanilla recipes can't output NBT items, and two packs sharing them would clash.\n\nSo ", "color": "white"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": " quietly routes any recipe touching custom items through ", "color": "white"}, {"text": "Smithed", "bold": true, "color": "aqua"}, {"text": " ", "color": "white"}, {"text": "Crafter", "bold": true, "color": "aqua"}, {"text": " and ", "color": "white"}, {"text": "Furnace NBT Recipes", "bold": true, "color": "aqua"}, {"text": ".\n\n", "color": "white"}, {"text": "You write one recipe. It picks the engine.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000006 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000006 transformation.scale set value [0.5f, 0.5f, 0.5f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000006 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000006 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000006 height set value 0.0f

