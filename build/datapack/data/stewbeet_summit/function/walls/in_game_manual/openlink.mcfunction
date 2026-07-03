
#> stewbeet_summit:walls/in_game_manual/openlink
#
# @executed	positioned 202.5 101.0 -24.5 & rotated 180 0
#
# @within	stewbeet_summit:walls/setup [ positioned 202.5 101.0 -24.5 & rotated 180 0 ]
#

execute if score #in_game_manual stewbeet_summit.page matches 0 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "In-Game Manual", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Free Documentation", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Please check the GIF! I highly recommend it!!!", "color": "#8BE9FD"}], "tooltip": {"text": "https://github.com/Stoupy51/StewBeet/blob/main/docs/plugins/img/ingame_manual.gif", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://github.com/Stoupy51/StewBeet/blob/main/docs/plugins/img/ingame_manual.gif"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}
execute if score #in_game_manual stewbeet_summit.page matches 2 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "In-Game Manual", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Always Up To Date", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Docs: In-Game Manual", "color": "#8BE9FD"}], "tooltip": {"text": "https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

