
# Imports
from stewbeet import *  # type: ignore


# Main entry point
def main():
    ns: str = Mem.ctx.project_id

    # Add items to the definitions
    Item(id="bg_black_hole", override_model={"parent":"minecraft:block/cube_all"})
    Item(id="logo", override_model={"parent":"minecraft:item/generated"})

    # 3D items
    for item in ["arrow", "title"]:
        model = stp.json_load(Mem.ctx.directory / f"assets/{item}.json")
        model["textures"]["0"] = f"{ns}:item/{item}"
        Item(id=item, override_model=model)

    pass

