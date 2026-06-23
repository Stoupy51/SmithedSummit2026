
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
        "Tags": [f"{ns}.{item}", "summit.static"],
        **kwargs
    }


# Main entry point (ran just before making finalyzing the build process (zip, headers, lang, ...))
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id  # type: ignore # noqa: F841

    # Blackhole
    black_hole: str = "20180612-2026-2002-2098-201000000000"
    black_hole_nbt: JsonDict = item_nbt("bg_black_hole", transformation=scale_only(16.69, 9.69, -18.69))

    # Logo
    logo: str = "20180612-2026-2002-2098-201000000001"
    logo_nbt: JsonDict = item_nbt("logo", transformation=scale_only(2.0, 2.0, 2.0), Rotation=[180,0])


    # You can either write your mcfunction files in src/data/... or with the python way:
    # Add some commands when loading datapack
    write_load_file(f"""
# Summon a Black Hole underground
execute unless entity {black_hole} run summon minecraft:item_display 198.5 54.0 -21.5 {{UUID:uuid("{black_hole}"),{json.dumps(black_hole_nbt)[1:-1]}}}

# Summon the logo at entrance
execute unless entity {logo} run summon minecraft:item_display 197.0 98.0 -9.0 {{UUID:uuid("{logo}"),{json.dumps(logo_nbt)[1:-1]}}}
""")

    pass

