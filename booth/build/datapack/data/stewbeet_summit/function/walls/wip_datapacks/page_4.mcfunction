
#> stewbeet_summit:walls/wip_datapacks/page_4
#
# @within	stewbeet_summit:walls/wip_datapacks/show
#

# Page 5/6 "Loadouts": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000013 text set value ["", {"text": "Loadouts & classes (5/6)\n\n", "bold": true, "color": "gold"}, {"text": "Build your class with ", "color": "white"}, {"text": "pick-10", "bold": true, "color": "aqua"}, {"text": " style constraints and perk selection.\n\n", "color": "white"}, {"text": "Browse a ", "color": "white"}, {"text": "marketplace", "bold": true, "color": "aqua"}, {"text": " of player-made loadouts: filter, favorite, share public or keep private.", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000013 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000013 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000013 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000013 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000013 height set value 0.0f

