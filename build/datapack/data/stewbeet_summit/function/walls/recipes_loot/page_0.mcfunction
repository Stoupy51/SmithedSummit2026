
#> stewbeet_summit:walls/recipes_loot/page_0
#
# @within	stewbeet_summit:walls/recipes_loot/show
#

# Page 1/6 "Recipes Live on the Item": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000006 text set value ["", {"text": "Recipes as objects (1/6)\n\n", "bold": true, "color": "gold"}, {"text": "No recipe JSON. No advancement wiring. Just hand the item its recipes:\n\n", "color": "white"}, ["", {"text": "Item", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "id", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "\"ruby_sword\"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": "recipes", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "[", "color": "#F8F8F2"}, {"text": "CraftingShapedRecipe", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "shape", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "[", "color": "#F8F8F2"}, {"text": "\" R \"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\" R \"", "color": "#F1FA8C"}, {"text": ",", "color": "#F8F8F2"}, {"text": "\" S \"", "color": "#F1FA8C"}, {"text": "],", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "ingredients", "color": "#F8F8F2"}, {"text": "=", "color": "#FF79C6"}, {"text": "{", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "            "}, {"text": "\"R\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "Ingr", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"ruby\"", "color": "#F1FA8C"}, {"text": "),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "            "}, {"text": "\"S\"", "color": "#F1FA8C"}, {"text": ":", "color": "#F8F8F2"}, {"text": " "}, {"text": "Ingr", "color": "#8BE9FD"}, {"text": "(", "color": "#F8F8F2"}, {"text": "\"minecraft:stick\"", "color": "#F1FA8C"}, {"text": "),", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "        "}, {"text": "},", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": "    "}, {"text": ")],", "color": "#F8F8F2"}, {"text": "\n"}], ["", {"text": ")", "color": "#F8F8F2"}]]
data modify entity 20180612-2026-2002-2098-202000000006 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000006 transformation.scale set value [0.42f, 0.42f, 0.42f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000006 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000006 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000006 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000006 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000006 height set value 0.0f

