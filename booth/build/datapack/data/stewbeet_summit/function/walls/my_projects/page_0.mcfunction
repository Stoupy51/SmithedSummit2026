
#> stewbeet_summit:walls/my_projects/page_0
#
# @within	stewbeet_summit:walls/my_projects/show
#

# Page 1/1 "My Projects": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000010 text set value ["", {"text": "My Projects\n\n", "bold": true, "color": "gold"}, {"text": "Welcome to the Switch Space!\nYou'll find a variety of my projects here, all built on ", "color": "white"}, [{"text": "S", "color": "#ff9100", "italic": false}, {"text": "t", "color": "#ff7c00"}, {"text": "e", "color": "#ff6700"}, {"text": "w", "color": "#ff5200"}, {"text": "B", "color": "#ff3e00"}, {"text": "e", "color": "#ff2900"}, {"text": "e", "color": "#ff1400"}, {"text": "t", "color": "#ff0000"}], {"text": ".\n\n", "color": "white"}, {"text": "This black hole is a part of the lobby of my project ", "color": "white"}, {"text": "Switch Minigames", "bold": true, "color": "aqua"}, {"text": ", check the zone on the right for more details.\n\n", "color": "white"}, {"text": "The 3 other zones are split in 3 categories:\n", "color": "white"}, {"text": "- My ", "color": "white"}, {"text": "released", "bold": true, "color": "aqua"}, {"text": " datapacks\n", "color": "white"}, {"text": "- My ", "color": "white"}, {"text": "WIP", "bold": true, "color": "aqua"}, {"text": " datapacks\n", "color": "white"}, {"text": "- Myself, the developer", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000010 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000010 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000010 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000010 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

