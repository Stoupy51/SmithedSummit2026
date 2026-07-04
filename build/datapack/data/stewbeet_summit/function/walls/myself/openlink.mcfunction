
#> stewbeet_summit:walls/myself/openlink
#
# @executed	positioned 191.5 53.0 -20.5 & rotated -90 0
#
# @within	stewbeet_summit:walls/setup [ positioned 191.5 53.0 -20.5 & rotated -90 0 ]
#

# Open the current page's link dialog (@s is the clicking player thanks to the
# 'execute on target run' in the interaction's callback). The dialog is inlined as
# SNBT so it needs no server restart; linkless pages have no branch (their
# "Open link" hitbox is 0-sized anyway, so this function cannot fire on them)
execute if score #myself stewbeet_summit.page matches 0 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Myself", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Who Am I?", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "github.com/Stoupy51", "color": "#8BE9FD"}], "tooltip": {"text": "https://github.com/Stoupy51", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://github.com/Stoupy51"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}
execute if score #myself stewbeet_summit.page matches 2 run dialog show @s {"type": "minecraft:multi_action", "title": {"text": "Myself", "bold": true, "color": "#FFD479"}, "body": [{"type": "minecraft:plain_message", "width": 240, "contents": {"text": "Always Building", "color": "gray"}}], "columns": 1, "actions": [{"label": ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "github.com/Stoupy51", "color": "#8BE9FD"}], "tooltip": {"text": "https://github.com/Stoupy51", "color": "gray"}, "width": 240, "action": {"type": "open_url", "url": "https://github.com/Stoupy51"}}], "exit_action": {"label": {"text": "Close", "color": "red"}}, "can_close_with_escape": true}

