
#> stewbeet_summit:walls/material_sets/page_6
#
# @within	stewbeet_summit:walls/material_sets/show
#

# Page 7/9 "Pick Your Tier": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000007 text set value ["", {"text": "Any vanilla tier (7/9)\n\n", "bold": true, "color": "gold"}, {"text": "Base the set on any tier: ", "color": "white"}, {"text": "wood", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "stone", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "gold", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "copper", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "iron", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "diamond", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "netherite", "bold": true, "color": "aqua"}, {"text": ".\n\n", "color": "white"}, {"text": "Modifiers auto-route: ", "color": "white"}, {"text": "armor & toughness to ", "color": "white"}, {"text": "armor", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "damage & mining to ", "bold": true, "color": "aqua"}, {"text": "tools", "bold": true, "color": "aqua"}, {"text": ".\n\n", "color": "white"}, {"text": "Stone -> chainmail armor,\nwood -> leather armor.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000007 line_width set value 195
data modify entity 20180612-2026-2002-2098-202000000007 transformation.scale set value [0.55f, 0.55f, 0.55f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000007 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000007 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000007 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000007 height set value 0.0f

