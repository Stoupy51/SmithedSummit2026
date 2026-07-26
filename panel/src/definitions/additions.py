
# ruff: noqa: E501
# Imports
from stewbeet import *  # type: ignore


# Main entry point
def main():
    """ Register every custom item of the pack into Mem.definitions. """
    #ns: str = Mem.ctx.project_id

    # Add items to the definitions
    Item(id="tomato", components={
        "profile": {"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzhiNzUyZTUyMzJiMDM5YjFlNzVlNDU0MTgzYTE5MmQ0MDU3YjdjYTgzMmY3YzI0YTVmZDg2Nzk2OWNiNGQifX19"}]},
    })

