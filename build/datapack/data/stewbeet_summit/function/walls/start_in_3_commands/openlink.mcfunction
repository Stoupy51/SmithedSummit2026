
#> stewbeet_summit:walls/start_in_3_commands/openlink
#
# @executed	positioned 201.5 101.0 -19.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 201.5 101.0 -19.5 & rotated 180 0 ]
#

# Open the current page's link dialog (@s is the clicking player thanks to the
# 'execute on target run' in the interaction's callback). The dialog is inlined as
# SNBT so it needs no server restart; linkless pages have no branch (their
# "Open link" hitbox is 0-sized anyway, so this function cannot fire on them)
execute if score #start_in_3_commands stewbeet_summit.page matches 0 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Start in 3 Commands", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Install", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Getting Started", "color": "#8BE9FD"}], "tooltip": {"text": "https://stewbeet.paralya.fr/markdown?src=0_getting_started%2Fen.md", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=0_getting_started%2Fen.md"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

