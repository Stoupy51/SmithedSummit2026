
#> stewbeet_summit:walls/switch_minigames/openlink
#
# @executed	positioned 198.5 53.0 -27.5 & rotated 0 0
#
# @within	stewbeet_summit:walls/setup [ positioned 198.5 53.0 -27.5 & rotated 0 0 ]
#

# Open the current page's link dialog (@s is the clicking player thanks to the
# 'execute on target run' in the interaction's callback). The dialog is inlined as
# SNBT so it needs no server restart; linkless pages have no branch (their
# "Open link" hitbox is 0-sized anyway, so this function cannot fire on them)
execute if score #switch_minigames stewbeet_summit.page matches 0 run return run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Switch Minigames", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Switch Minigames", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.discord"}, {"text": " "}, {"text": "Be notified of updates", "color": "#8BE9FD"}], "tooltip": {"text": "https://discord.gg/anxzu6rA9F", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://discord.gg/anxzu6rA9F"}}, {"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Terrifying source code", "color": "#8BE9FD"}], "tooltip": {"text": "https://github.com/Paralya/Switch", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://github.com/Paralya/Switch"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}
execute if score #switch_minigames stewbeet_summit.page matches 2 run return run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Switch Minigames", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "The Minigames", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.youtube"}, {"text": " "}, {"text": "2 years of memories (video)", "color": "#8BE9FD"}], "tooltip": {"text": "https://www.youtube.com/watch?v=cB27sEOxboA", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://www.youtube.com/watch?v=cB27sEOxboA"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

