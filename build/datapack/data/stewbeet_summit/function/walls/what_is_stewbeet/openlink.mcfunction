
#> stewbeet_summit:walls/what_is_stewbeet/openlink
#
# @executed	positioned 211.5 101.0 -18.5 & rotated 90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 211.5 101.0 -18.5 & rotated 90 0 ]
#

# Open the current page's link dialog (@s is the clicking player thanks to the
# 'execute on target run' in the interaction's callback). The dialog is inlined as
# SNBT so it needs no server restart; linkless pages have no branch (their
# "Open link" hitbox is 0-sized anyway, so this function cannot fire on them)
execute if score #what_is_stewbeet stewbeet_summit.page matches 0 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "What is StewBeet?", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Introduction", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "stewbeet.paralya.fr", "color": "#8BE9FD"}], "tooltip": {"text": "https://stewbeet.paralya.fr", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://stewbeet.paralya.fr"}}, {"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.discord"}, {"text": " "}, {"text": "discord.gg/anxzu6rA9F", "color": "#8BE9FD"}], "tooltip": {"text": "https://discord.gg/anxzu6rA9F", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://discord.gg/anxzu6rA9F"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

