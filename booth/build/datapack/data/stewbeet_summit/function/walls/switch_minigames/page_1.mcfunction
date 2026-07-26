
#> stewbeet_summit:walls/switch_minigames/page_1
#
# @within	stewbeet_summit:walls/switch_minigames/show
#

# Page 2/3 "The Vote": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000011 text set value ["", {"text": "Democracy! (2/3)\n\n", "bold": true, "color": "gold"}, {"text": "At the end of each round, a ", "color": "white"}, {"text": "vote", "bold": true, "color": "aqua"}, {"text": " decides the next minigame (7 options):\n\n", "color": "white"}, {"text": "- Option 1 replays the last game,\n  great for a loop of ", "color": "white"}, {"text": "fuuuun", "bold": true, "color": "gold"}, {"text": "\n", "color": "white"}, {"text": "- Options 2-7 are random picks based on the player count\n", "color": "white"}, {"text": "- The 7th hides its pick under the name ", "color": "white"}, {"text": "\"Random\"", "bold": true, "color": "aqua"}, {"text": "\n\n", "color": "white"}, {"text": "15 seconds to vote,\nchange it anytime until the end.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000011 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000011 transformation.scale set value [0.45f, 0.45f, 0.45f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000011 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000011 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# No link on this page: blank the "Open link" prompt and shrink its hitbox to 0 (unclickable)
data modify entity 20180612-2026-2002-2098-202300000011 text set value ["", {"text": ""}]
data modify entity 20180612-2026-2002-2098-202400000011 width set value 0.0f
data modify entity 20180612-2026-2002-2098-202400000011 height set value 0.0f

