
#> stewbeet_summit:walls/what_is_stewbeet/openlink
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 211.5 101.0 -18.5 & rotated 90 0 ]
#

execute if score #what_is_stewbeet stewbeet_summit.page matches 0 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "What is StewBeet?", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Introduction", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "stewbeet.paralya.fr", "color": "#8BE9FD"}], "tooltip": {"text": "https://stewbeet.paralya.fr", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://stewbeet.paralya.fr"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

