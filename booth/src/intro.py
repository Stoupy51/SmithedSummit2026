""" StewBeet Summit 2026 - entrance decorations plugin.

beet pipeline entry (referenced as `src.intro` in beet.yml). Independent of the
presentation walls (src/walls): it summons the decorative displays at the summit
entrance - background black hole, logo, title and two arrows - into intro/setup,
called from entities/summon (src/booth.py). Each summon is guarded by a fixed UUID
(`execute unless entity ...`) so re-running on every /reload never duplicates them.
"""

# Imports
from beet import Context
from stewbeet import Mem, write_function
from stouputils.typing import JsonDict

from .utils.nbt import dump, item_nbt, scale_only


# Main entry point (runs before the build is finalized: zip, headers, lang, ...).
def beet_default(ctx: Context) -> None:
	""" Write intro/setup: summon the summit entrance decorations if absent. """
	ns: str = Mem.ctx.project_id
	# Background black hole (placed underground)
	black_hole: str = "20180612-2026-2002-2098-201000000000"
	black_hole_nbt: JsonDict = item_nbt("bg_black_hole", transformation=scale_only(16.69, 9.8, -16.69))

	# Logo
	logo: str = "20180612-2026-2002-2098-201000000001"
	logo_nbt: JsonDict = item_nbt("logo", transformation=scale_only(2.5, 2.5, 5.0), Rotation=[180, 0])

	# Title
	title: str = "20180612-2026-2002-2098-201000000002"
	title_nbt: JsonDict = item_nbt("title", transformation=scale_only(3.5, 3.5, 3.5), Rotation=[0, 0])

	# Two arrows (one slightly tilted, one rotated flat)
	arrow_1: str = "20180612-2026-2002-2098-201000000003"
	arrow_2: str = "20180612-2026-2002-2098-201000000004"
	arrow_trans_1: JsonDict = scale_only(5.0, 5.0, 5.0)
	arrow_trans_1["left_rotation"] = [0.0, 0.0, 0.172, 0.985]
	arrow_nbt_1: JsonDict = item_nbt("arrow", transformation=arrow_trans_1)
	arrow_nbt_2: JsonDict = item_nbt("arrow", transformation=scale_only(5.0, 5.0, 2.5), Rotation=[-90, 0])

	# Logo & Title at the real entrance
	logo_2: str = "20180612-2026-2002-2098-201000000005"
	logo_2_nbt: JsonDict = item_nbt("logo", transformation=scale_only(2.5, 2.5, 5.0), Rotation=[90, 0])
	title_2: str = "20180612-2026-2002-2098-201000000006"
	title_2_nbt: JsonDict = item_nbt("title", transformation=scale_only(2, 2, 2), Rotation=[-90, 0])

	# Button to get out of the underground
	underground_button: str = "20180612-2026-2002-2098-201000000007"
	underground_button_nbt: JsonDict = item_nbt("underground_button", transformation=scale_only(1.5, 1.5, 1.5), Rotation=[0, 0])
	underground_button_nbt["item"]["id"] = "minecraft:pale_oak_button"
	underground_interaction: str = "20180612-2026-2002-2098-201000000008"
	underground_interaction_nbt: JsonDict = {
		"Tags": [f"summit.booth_entity.{ns}", f"{ns}.entity", "summit.static", "summit.interactable"],
		"response": True, "width": 1.2, "height": 1.2,
		"data": {"summit_interactable": {"on_right_click": "execute on target run effect give @s levitation 4 13 true"}}
	}
	del underground_button_nbt["item"]["components"]

	# Stoupy Mannequin
	stoupy_mannequin: str = "20180612-2026-2002-2098-201000000009"
	stoupy_mannequin_nbt: JsonDict = item_nbt("stoupy_mannequin", Rotation=[225, 0])
	del stoupy_mannequin_nbt["item"]
	del stoupy_mannequin_nbt["brightness"]
	stoupy_mannequin_nbt.update({"profile": {"id":[-1801187418,-255572281,-1865653756,408220292],"name":"Stoupy51","properties":[{"name":"textures","signature":"kYXn5aJ/ALBmrY8rZXiU/wf7WWEukFAipXrTyR2bsKH9daA4MFQ5UAAsAY8QF8fP1wNvd33jAlyjhVlqsy6REsiCp950Y4ogxhkgYp4Sv15dlaovuJd6q0LSwemWVfFr9lFScKqBTrp72ylICjJu5HgXGELv3cKs2MUIiqCykpQQSB/uncYkwaEu3amtrx7QOvhQOIelFPUX1didTglrYbdwc9U29vDiExkvIXrKutBSExLgW1mTXTXW/5F5FGOSQ+ZNuJpBonLMMQa7u2AtCtZ/HuY6bYfiJsK1tZtNzDvv0keuCk0EWxLiRmeZ0BE0oc0MAG+6OpN8mpBFSvilkhYzxQNIAOfzDmnbd8X9v/3Vc5YyjBRusFiz9YbQUNBJFVCqerNzP+wu5s6gj242ecORk2ftDOcwSGjFsOpOHqdtLObwl5pUPs1rpGjVlRWrJTs2xA5cG6drL2rAGeW3k8cafOTNZjDI3O70MQRTpuGg0H5kYJawtfwuJ36q1jFZY5ZA95+AtfWbr0IL7/uKH2ilomn1lO1JJ+4yQw99hyjc2xM+T1cnRrARPGjX97SvXHfKDLqZl1lbM2V79jUol0jTmYeC9L/1Pid6grPudvwIDIf4hlng4xVJrLMkBdVrdeymK4aAyqTcTkttVlGj0Y+shCa+AgVRDdXOjIMpheY=","value":"ewogICJ0aW1lc3RhbXAiIDogMTc4MzIwMDkzNjc4NywKICAicHJvZmlsZUlkIiA6ICI5NGE0MGZhNmYwYzQ0NmM3OTBjYzYyMDQxODU0ZjI4NCIsCiAgInByb2ZpbGVOYW1lIiA6ICJTdG91cHk1MSIsCiAgInNpZ25hdHVyZVJlcXVpcmVkIiA6IHRydWUsCiAgInRleHR1cmVzIiA6IHsKICAgICJTS0lOIiA6IHsKICAgICAgInVybCIgOiAiaHR0cDovL3RleHR1cmVzLm1pbmVjcmFmdC5uZXQvdGV4dHVyZS9iMmRjMDk1NGM3YTg3NDc2NWE1Y2Y5MDU3MTQ0NWM0ZWJiOWM3MTA1MDA0ZDU4YThhMzc0NTYzMDQ1MTFlYzk1IiwKICAgICAgIm1ldGFkYXRhIiA6IHsKICAgICAgICAibW9kZWwiIDogInNsaW0iCiAgICAgIH0KICAgIH0sCiAgICAiQ0FQRSIgOiB7CiAgICAgICJ1cmwiIDogImh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYWZkNTUzYjM5MzU4YTI0ZWRmZTNiOGE5YTkzOWZhNWZhNGZhYTRkOWE5YzNkNmFmOGVhZmIzNzdmYTA1YzJiYiIKICAgIH0KICB9Cn0="}]}, "NoAI": True, "Invulnerable": True})  # noqa: E501

	# Write the intro/setup function
	write_function(f"{ns}:intro/setup", f"""
# Background black hole (underground)
execute unless entity {black_hole} run summon item_display 198.5 54.0 -20.5 {{UUID:uuid("{black_hole}"),{dump(black_hole_nbt)}}}

# Logo, title, and arrows at the entrance
execute unless entity {logo} run summon item_display 196.5 103.5 -9.9 {{UUID:uuid("{logo}"),{dump(logo_nbt)}}}
execute unless entity {title} run summon item_display 196.5 103.0 -9.6 {{UUID:uuid("{title}"),{dump(title_nbt)}}}
execute unless entity {arrow_1} run summon item_display 197.6875 99.4375 -10.5 {{UUID:uuid("{arrow_1}"),{dump(arrow_nbt_1)}}}
execute unless entity {arrow_2} run summon item_display 198.9375 98.125 -4.0 {{UUID:uuid("{arrow_2}"),{dump(arrow_nbt_2)}}}

# Another time the logo and title at the real entrance
execute unless entity {logo_2} run summon item_display 207.0 103.5 -16.0 {{UUID:uuid("{logo_2}"),{dump(logo_2_nbt)}}}
execute unless entity {title_2} run summon item_display 207.25 102.5 -16.0 {{UUID:uuid("{title_2}"),{dump(title_2_nbt)}}}

# Button to get out of the underground
execute unless entity {underground_button} run summon item_display 210.0 52.5 -26.0 {{UUID:uuid("{underground_button}"),{dump(underground_button_nbt)}}}
execute unless entity {underground_interaction} run summon interaction 210.0 52.5 -26.0 {{UUID:uuid("{underground_interaction}"),{dump(underground_interaction_nbt)}}}

# Stoupy Mannequin (deferred: even with its death animation fast-forwarded in
# entities/kill, the freshly killed corpse still holds the UUID this tick)
schedule function {ns}:intro/mannequin 2t replace
""", overwrite=True)

	# The mannequin summon itself, run 2 ticks after intro/setup (see above).
	write_function(f"{ns}:intro/mannequin", f"""
# Stoupy Mannequin
execute unless entity {stoupy_mannequin} run summon mannequin 192 53 -19 {{UUID:uuid("{stoupy_mannequin}"),{dump(stoupy_mannequin_nbt)}}}
""", overwrite=True)

