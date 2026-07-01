""" StewBeet Summit 2026 - entrance decorations plugin.

beet pipeline entry (referenced as `src.intro` in beet.yml). Independent of the
presentation walls (src/walls): it summons the decorative displays at the summit
entrance - background black hole, logo, title and two arrows - into intro/setup,
then calls it from the load file. Each summon is guarded by a fixed UUID
(`execute unless entity ...`) so re-running on every /reload never duplicates them.
"""

# Imports
from beet import Context
from stewbeet import Mem, write_function, write_load_file
from stouputils.typing import JsonDict

from .utils.nbt import dump, item_nbt, scale_only


def setup_entrance(ns: str) -> None:
	""" Write intro/setup: summon the summit entrance decorations if absent. """
	# Background black hole (placed underground).
	black_hole: str = "20180612-2026-2002-2098-201000000000"
	black_hole_nbt: JsonDict = item_nbt("bg_black_hole", transformation=scale_only(16.69, 9.69, -18.69))

	# Logo.
	logo: str = "20180612-2026-2002-2098-201000000001"
	logo_nbt: JsonDict = item_nbt("logo", transformation=scale_only(2.5, 2.5, 4.0), Rotation=[180, 0])

	# Title.
	title: str = "20180612-2026-2002-2098-201000000002"
	title_nbt: JsonDict = item_nbt("title", transformation=scale_only(3.5, 3.5, 3.5), Rotation=[0, 0])

	# Two arrows (one slightly tilted, one rotated flat).
	arrow_1: str = "20180612-2026-2002-2098-201000000003"
	arrow_2: str = "20180612-2026-2002-2098-201000000004"
	arrow_trans_1: JsonDict = scale_only(5.0, 5.0, 5.0)
	arrow_trans_1["left_rotation"] = [0.0, 0.0, 0.172, 0.985]
	arrow_nbt_1: JsonDict = item_nbt("arrow", transformation=arrow_trans_1)
	arrow_nbt_2: JsonDict = item_nbt("arrow", transformation=scale_only(5.0, 5.0, 2.5), Rotation=[-90, 0])

	write_function(f"{ns}:intro/setup", f"""
# Background black hole (underground)
execute unless entity {black_hole} run summon minecraft:item_display 198.5 54.0 -21.5 {{UUID:uuid("{black_hole}"),{dump(black_hole_nbt)}}}

# Logo, title, and arrows at the entrance
execute unless entity {logo} run summon minecraft:item_display 196.5 103.5 -9.9 {{UUID:uuid("{logo}"),{dump(logo_nbt)}}}
execute unless entity {title} run summon minecraft:item_display 196.5 103.0 -9.6 {{UUID:uuid("{title}"),{dump(title_nbt)}}}
execute unless entity {arrow_1} run summon minecraft:item_display 197.6875 99.4375 -10.5 {{UUID:uuid("{arrow_1}"),{dump(arrow_nbt_1)}}}
execute unless entity {arrow_2} run summon minecraft:item_display 198.9375 98.125 -4.0 {{UUID:uuid("{arrow_2}"),{dump(arrow_nbt_2)}}}
""", overwrite=True)


# Main entry point (runs before the build is finalized: zip, headers, lang, ...).
def beet_default(ctx: Context) -> None:
	ns: str = Mem.ctx.project_id
	setup_entrance(ns)

	# Load: clear the previous decorations (they are UUID-guarded, so intro/setup
	# only re-summons the missing ones) and place them.
	# TODO: drop the kill when the summit build is finalized.
	write_load_file(f"""
# Entrance decorations (StewBeet)
kill @e[tag={ns}.entity]
function {ns}:intro/setup
""")
