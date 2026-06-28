
# Imports
import json

from beet import Context
from stewbeet import *  # type: ignore


# Utility functions
def scale_only(sx: float, sy: float, sz: float) -> JsonDict:
    return {
        "left_rotation":[0.0, 0.0, 0.0, 1.0],
        "right_rotation": [0.0, 0.0, 0.0, 1.0],
        "scale": [sx, sy, sz],
        "translation": [0.0, 0.0, 0.0]
    }

def item_nbt(item: str, **kwargs: Any) -> JsonDict:
    ns: str = Mem.ctx.project_id
    return {
        "item":{
            "id": "stone",
            "components": {"minecraft:item_model":f"{ns}:{item}"},
            "count": 1,
        },
        "Tags": [f"{ns}.{item}", f"{ns}.static", "summit.static"],
        "brightness": {"block": 15, "sky": 15},
        **kwargs
    }

def dump(obj: Any) -> str:
    return json.dumps(obj)[1:-1]


# Main entry point (ran just before making finalyzing the build process (zip, headers, lang, ...))
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id  # type: ignore

    # Blackhole
    black_hole: str = "20180612-2026-2002-2098-201000000000"
    black_hole_nbt: JsonDict = item_nbt("bg_black_hole", transformation=scale_only(16.69, 9.69, -18.69))

    # Logo
    logo: str = "20180612-2026-2002-2098-201000000001"
    logo_nbt: JsonDict = item_nbt("logo", transformation=scale_only(2.5, 2.5, 4.0), Rotation=[180,0])

    # Title
    title: str = "20180612-2026-2002-2098-201000000002"
    title_nbt: JsonDict = item_nbt("title", transformation=scale_only(3.5, 3.5, 3.5), Rotation=[0,0])

    # Arrow
    arrow_1: str = "20180612-2026-2002-2098-201000000003"
    arrow_2: str = "20180612-2026-2002-2098-201000000004"
    arrow_trans_1: JsonDict = scale_only(5.0, 5.0, 5.0)
    arrow_trans_1["left_rotation"] = [0.0, 0.0, 0.172, 0.985]
    arrow_nbt_1: JsonDict = item_nbt("arrow", transformation=arrow_trans_1)
    arrow_nbt_2: JsonDict = item_nbt("arrow", transformation=scale_only(5.0, 5.0, 2.5), Rotation=[-90,0])


    # You can either write your mcfunction files in src/data/... or with the python way:
    # Add some commands when loading datapack
    write_load_file(f"""
# TODO: remove
kill @e[tag={ns}.static]

# Summon a Black Hole underground
execute unless entity {black_hole} run summon minecraft:item_display 198.5 54.0 -21.5 {{UUID:uuid("{black_hole}"),{dump(black_hole_nbt)}}}

# Summon the logo, title, and arrow at entrance
execute unless entity {logo} run summon minecraft:item_display 196.5 103.5 -9.9 {{UUID:uuid("{logo}"),{dump(logo_nbt)}}}
execute unless entity {title} run summon minecraft:item_display 196.5 103.0 -9.6 {{UUID:uuid("{title}"),{dump(title_nbt)}}}
execute unless entity {arrow_1} run summon minecraft:item_display 197.6875 99.4375 -10.5 {{UUID:uuid("{arrow_1}"),{dump(arrow_nbt_1)}}}
execute unless entity {arrow_2} run summon minecraft:item_display 198.9375 98.125 -4.0 {{UUID:uuid("{arrow_2}"),{dump(arrow_nbt_2)}}}
""")

    pass

