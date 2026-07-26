
#> stewbeet_summit:walls/qol_ecosystem/page_2
#
# @within	stewbeet_summit:walls/qol_ecosystem/show
#

# Page 3/6 "Ship It": swap this page's text, wrap width and text scale into the display
data modify entity 20180612-2026-2002-2098-202000000009 text set value ["", {"text": "From build to release (3/6)\n\n", "bold": true, "color": "gold"}, {"text": "- Merge with ", "color": "white"}, {"text": "Smithed Weld\n ", "bold": true, "color": "aqua"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[merge_smithed_weld]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/merge_smithed_weld.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/merge_smithed_weld.md"}}], {"text": "\n\n- ", "color": "white"}, {"text": "SHA1", "bold": true, "color": "aqua"}, {"text": " hashes for servers\n ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[compute_sha1]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/compute_sha1.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/compute_sha1.md"}}], {"text": "\n\n- Auto-copy (works with ", "color": "white"}, {"text": "sftp", "bold": true, "color": "aqua"}, {"text": " too)\n ", "color": "white"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[copy_to_destination]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=plugins/copy_to_destination.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=plugins/copy_to_destination.md"}}], {"text": "\n\n- Continuous Delivery\n", "color": "white"}, {"text": "(Modrinth, Smithed, PMC, GitHub)\n ", "bold": true, "color": "aqua"}, ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "[Full Detailed Guide]", "color": "#8BE9FD", "underlined": true, "click_event": {"action": "open_url", "url": "https://stewbeet.paralya.fr/markdown?src=6_continuous_delivery%2Fen.md"}, "hover_event": {"action": "show_text", "value": "Open https://stewbeet.paralya.fr/markdown?src=6_continuous_delivery%2Fen.md"}}], {"text": "\n\nReady to publish in one command.", "color": "#7F8C99", "italic": true}]
data modify entity 20180612-2026-2002-2098-202000000009 line_width set value 220
data modify entity 20180612-2026-2002-2098-202000000009 transformation.scale set value [0.425f, 0.425f, 0.425f]

# Gray the arrow that has no page beyond it (left on the first page, right on the last)
data modify entity 20180612-2026-2002-2098-202100000009 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_left"
data modify entity 20180612-2026-2002-2098-202200000009 item.components."minecraft:item_model" set value "stewbeet_summit:nav_arrow_right"

# Refresh the centered "Open link" prompt and restore its clickable hitbox
data modify entity 20180612-2026-2002-2098-202300000009 text set value ["", {"font": "summit_icons:icons", "translate": "summit_icons.github"}, {"text": " "}, {"text": "Open link", "color": "#8BE9FD", "underlined": true}, {"text": " (+3)", "color": "gray"}]
data modify entity 20180612-2026-2002-2098-202400000009 width set value 0.75f
data modify entity 20180612-2026-2002-2098-202400000009 height set value 0.75f

