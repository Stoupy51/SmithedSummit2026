
#> stewbeet_summit:walls/zone2/page3
#
# @executed	positioned 201.5 101.0 -19.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/zone2/show
#

data modify entity @e[tag=stewbeet_summit.disp2,limit=1] text set value ["", {"text": "Bonus: auto-deploy\n\n", "bold": true, "color": "gold"}, {"text": "Point StewBeet at your world and it\n", "color": "white"}, {"text": "copies the build there on every run:\n\n", "color": "white"}, {"text": "build_copy_destinations:\n", "color": "#8BE9FD"}, {"text": "  datapack: [\".../datapacks\"]", "color": "#8BE9FD"}]
data modify entity @e[tag=stewbeet_summit.disp2,limit=1] line_width set value 260

