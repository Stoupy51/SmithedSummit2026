
# Imports
from beet import Context
from stewbeet import *  # type: ignore

# Additional imports (specific to this project)
from .definitions.additions import main as main_additions


# Main entry point
def beet_default(ctx: Context):
    """ Register the pack's item definitions and apply the finishing passes. """

    # Run additional definitions modifications (src/definitions/additions.py)
    main_additions()

    # Final adjustments
    add_item_model_component(black_list=["tomato"])
    add_item_name_and_lore_if_missing()
    add_private_custom_data_for_namespace()
    add_smithed_ignore_vanilla_behaviours_convention()

    # Debug purposes: export all definitions to a single json file
    export_all_definitions_to_json(f"{Mem.ctx.directory}/definitions_debug.json")

