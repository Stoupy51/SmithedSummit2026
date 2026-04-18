
# Imports
import json

from beet import Context
from stewbeet import *  # type: ignore


# Main entry point (ran just before making finalyzing the build process (zip, headers, lang, ...))
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id

    # Blackhole
    black_hole_nbt: JsonDict = {
        "item":{
            "id": "minecraft:stone",
            "components": {"minecraft:item_model":f"{ns}:black_hole"},
            "count": 1,
        },
        "transformation":{
            "left_rotation":[0.0, 0.0, 0.0, 1.0],
            "right_rotation": [0.0, 0.0, 0.0, 1.0],
            "scale": [16.69, 9.69, -18.69],
            "translation": [0.0, 0.0, 0.0]
        }
    }


    # You can either write your mcfunction files in src/data/... or with the python way:
    # Add some commands when loading datapack
    write_load_file(f"""
# Summon a Black Hole underground
summon minecraft:item_display 198.5 54.0 -21.5 {json.dumps(black_hole_nbt)}

""")

    pass

