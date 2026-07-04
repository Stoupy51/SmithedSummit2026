""" StewBeet Summit 2026 - item definitions plugin.

beet pipeline entry (referenced as `src.setup_definitions` in beet.yml, first in
the pipeline). Registers every custom item of the pack (src/definitions/) into
Mem.definitions, then applies the standard StewBeet finishing passes (item
models, names/lore, namespace data, Smithed conventions, manual components).
"""

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
    add_item_model_component()

    # Debug purposes: export all definitions to a single json file
    export_all_definitions_to_json(f"{Mem.ctx.directory}/definitions_debug.json")

