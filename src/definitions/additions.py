
# Imports
from stewbeet import *  # type: ignore


# Main entry point
def main():
    ns: str = Mem.ctx.project_id

    # Add items to the definitions
    # The black hole is a full cube whose faces are all mapped onto the SDK common
    # identifier pixel (column 0 of the 2x2 bg_black_hole texture) so the shader can
    # recognize the surface. UV [1,1,7,7] keeps every vertex inside that pixel.
    black_hole_faces: JsonDict = {
        face: {"uv": [1, 1, 7, 7], "texture": "#all"}
        for face in ("north", "east", "south", "west", "up", "down")
    }
    black_hole_model: JsonDict = {
        "textures": {"all": f"{ns}:item/bg_black_hole", "particle": f"{ns}:item/bg_black_hole"},
        "elements": [{"from": [0, 0, 0], "to": [16, 16, 16], "faces": black_hole_faces}],
    }
    Item(id="bg_black_hole", override_model=black_hole_model)
    Item(id="logo", override_model={"parent":"minecraft:item/generated"})

    # 3D items
    for item in ["arrow", "title"]:
        model = stp.json_load(Mem.ctx.directory / f"assets/{item}.json")
        model["textures"]["0"] = f"{ns}:item/{item}"
        Item(id=item, override_model=model)

    pass

