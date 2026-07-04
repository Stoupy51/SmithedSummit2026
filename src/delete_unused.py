

# Imports
from beet import Context
from stewbeet import *  # type: ignore


# Main entry point
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id
    version: str = Mem.ctx.project_version

    # Remove few lines in functions
    for path in (f"v{version}/load/secondary", f"v{version}/load/confirm_load"):
        f: Function = ctx.data[ns].functions[path]
        f.text = "\n".join(
            line for line in f.text.split("\n")
            if all(x not in line for x in ("set_items_storage", )) # TODO: add convention.debug
        )

    # Delete unnecessary functions
    del ctx.data[ns].functions[f"v{version}/load/set_items_storage"]

