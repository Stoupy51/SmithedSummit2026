
#> stewbeet_summit:walls/material_sets/openlink
#
# @executed	positioned 197.5 101.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 197.5 101.0 -27.5 & rotated 0 0 ]
#

execute if score #material_sets stewbeet_summit.page matches 8 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Material Sets", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Mix Anything", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: Definitions Setup", "color": "#8BE9FD"}], "tooltip": {"text": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

