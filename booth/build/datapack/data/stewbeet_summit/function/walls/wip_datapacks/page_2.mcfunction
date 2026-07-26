
#> stewbeet_summit:walls/wip_datapacks/page_2
#
# @within	stewbeet_summit:walls/wip_datapacks/show
#

# Page 3/6 "Game Modes": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000013 text set value ["", {"text": "Three game families (3/6)\n\n", "bold": true, "color": "gold"}, {"text": "- ", "color": "white"}, {"text": "Multiplayer", "bold": true, "color": "aqua"}, {"text": ": FFA, Team Deathmatch, Domination, Hardpoint, Search & Destroy\n\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "Missions", "bold": true, "color": "aqua"}, {"text": ": co-op PvE with waypoints navigation to targets\n\n", "color": "white"}, {"text": "- ", "color": "white"}, {"text": "Zombies", "bold": true, "color": "aqua"}, {"text": ": round-based survival with perks, mystery box, traps...", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000013 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000013 transformation.scale set value [0.6f, 0.6f, 0.6f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000013 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000013 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000013 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000013 height set value 0.0f

