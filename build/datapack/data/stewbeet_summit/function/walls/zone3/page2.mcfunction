
#> stewbeet_summit:walls/zone3/page2
#
# @executed	positioned 195.5 101.0 -11.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/zone3/show
#

data modify entity @e[tag=stewbeet_summit.disp3,limit=1] text set value ["", {"text": "Just drop a texture\n\n", "bold": true, "color": "gold"}, {"text": "Put ", "color": "white"}, {"text": "ruby.png", "bold": true, "color": "aqua"}, {"text": " in assets/textures/\n\n", "color": "white"}, {"text": "StewBeet auto-detects it and builds\n", "color": "white"}, {"text": "the model + item_model reference.\n\n", "color": "white"}, {"text": "No JSON model files by hand.", "color": "#7F8C99", "italic": true}]
data modify entity @e[tag=stewbeet_summit.disp3,limit=1] line_width set value 175

