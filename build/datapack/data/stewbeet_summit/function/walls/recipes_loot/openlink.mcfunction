
#> stewbeet_summit:walls/recipes_loot/openlink
#
# @executed	positioned 191.5 101.0 -22.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 191.5 101.0 -22.5 & rotated -90 0 ]
#

execute if score #recipes_loot stewbeet_summit.page matches 5 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Recipes & Loot", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Loot & Manual, For Free", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Definitions Setup", "color": "#8BE9FD"}], "tooltip": {"text": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

