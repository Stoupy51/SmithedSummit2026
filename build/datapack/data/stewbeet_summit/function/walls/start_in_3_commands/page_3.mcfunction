
#> stewbeet_summit:walls/start_in_3_commands/page_3
#
# @executed	positioned 201.5 101.0 -19.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/start_in_3_commands/show
#

data modify entity 20180612-2026-2002-2098-202000000002 text set value ["", {"text": "Bonus: auto-copy (4/4)\n\n", "bold": true, "color": "gold"}, {"text": "Point StewBeet at your world and resource pack folders and it copies the build there on every run:\n\n", "color": "white"}, {"text": "build_copy_destinations:\n", "color": "#8BE9FD"}, {"text": "  datapack: \n   - \".../datapacks\",\n   - \"sftp://user:pass@host/path\"\n\n", "color": "#8BE9FD"}, {"text": "  resource_pack: \n   - \"D:/minecraft/latest/resourcepacks\"\n\n", "color": "#8BE9FD"}, {"text": "(Works over SFTP too and password can be moved to a credentials file)", "color": "white"}]
data modify entity 20180612-2026-2002-2098-202000000002 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000002 transformation.scale set value [0.4, 0.4, 0.4]
data modify entity 20180612-2026-2002-2098-202100000002 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000002 item.components."minecraft:item_model" set value "stewbeet_summit:gray_nav_arrow_right"

