
#> stewbeet_summit:walls/zone7/page1
#
# @executed	positioned 197.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/zone7/show
#

data modify entity @e[tag=stewbeet_summit.disp7,limit=1] text set value ["", {"text": "Load and tick, handled\n\n", "bold": true, "color": "gold"}, {"text": "write_load_file(\"\"\"\n", "color": "#8BE9FD"}, {"text": "scoreboard objectives add\n", "color": "#8BE9FD"}, {"text": "    ruby.data dummy\n", "color": "#8BE9FD"}, {"text": "\"\"\")", "color": "#8BE9FD"}]
data modify entity @e[tag=stewbeet_summit.disp7,limit=1] line_width set value 260

