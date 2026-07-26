
#> stewbeet_summit:walls/wip_datapacks/page_1
#
# @within	stewbeet_summit:walls/wip_datapacks/show
#

# Page 2/6 "The Weapons": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000013 text set value ["", {"text": "The weapon framework (2/6)\n\n", "bold": true, "color": "gold"}, {"text": "- ", "color": "white"}, {"text": "Hit detection", "bold": true, "color": "aqua"}, {"text": " raycasts with spread & headshot detection\n", "color": "white"}, {"text": "- Slow projectiles (", "color": "white"}, {"text": "RPG", "bold": true, "color": "aqua"}, {"text": ") and throwable ", "color": "white"}, {"text": "grenades", "bold": true, "color": "aqua"}, {"text": "\n", "color": "white"}, {"text": "- Ammo, reload & reserve tracking\n", "color": "white"}, {"text": "- Fire modes: ", "color": "white"}, {"text": "semi", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "auto", "bold": true, "color": "aqua"}, {"text": ", ", "color": "white"}, {"text": "burst", "bold": true, "color": "aqua"}, {"text": "\n", "color": "white"}, {"text": "- Recoil & casing ejection\n", "color": "white"}, {"text": "- Lore generated from the stats", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000013 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000013 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000013 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000013 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000013 height set value 0.0f

