
#> stewbeet_summit:walls/zone3/page3
#
# @executed	positioned 195.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/zone3/show
#

data modify entity @e[tag=stewbeet_summit.disp3,limit=1] text set value ["", {"text": "One global registry\n\n", "bold": true, "color": "gold"}, {"text": "Every definition lives in ", "color": "white"}, {"text": "Mem.definitions", "bold": true, "color": "aqua"}, {"text": ".\n\n", "color": "white"}, {"text": "ruby = Item.from_id(\"ruby\")\n", "color": "#8BE9FD"}, {"text": "ruby.manual_category = \"materials\"", "color": "#8BE9FD"}]
data modify entity @e[tag=stewbeet_summit.disp3,limit=1] line_width set value 260

