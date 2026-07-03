""" The pack's custom item definitions.

Called by src.setup_definitions early in the pipeline. Every Item() registered
here lands in Mem.definitions, from which StewBeet generates the models, loot
tables and resource-pack entries. The items are all display props: the entrance
decorations (black hole, logo, title, arrows - summoned by src/intro.py) and
the presentation walls' nav arrows (used by src/walls).
"""

# Imports
from stewbeet import *  # type: ignore


# Main entry point
def main():
    """ Register every custom item of the pack into Mem.definitions. """
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
    Item(id="logo")

    # Flat navigation arrows for the presentation walls (placeholder textures).
    for grayed in ("", "gray_"):
        for side in ("left", "right"):
            Item(id=f"{grayed}nav_arrow_{side}")

    # 3D items whose models live in assets/<item>.json (texture 0 swapped to the
    # project's own texture).
    for item in ["arrow", "title"]:
        model = stp.json_load(Mem.ctx.directory / f"assets/{item}.json")
        model["textures"]["0"] = f"{ns}:item/{item}"
        Item(id=item, override_model=model)

