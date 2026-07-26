

# Imports
from beet import Context
from stewbeet import *  # type: ignore


# Main entry point
def beet_default(ctx: Context):
    ns: str = Mem.ctx.project_id
    version: str = Mem.ctx.project_version

    # Remove few lines in functions
    for path in (f"v{version}/load/secondary", f"v{version}/load/confirm_load"):
        if not ctx.data[ns].functions.get(path):
            continue
        f: Function = ctx.data[ns].functions[path]
        f.text = "\n".join(
            line for line in f.text.split("\n")
            if all(x not in line for x in ("set_items_storage", "convention.debug")) # TODO: add convention.debug
        )

    # Delete unnecessary functions
    if ctx.data[ns].functions.get(f"v{version}/load/set_items_storage"):
        del ctx.data[ns].functions[f"v{version}/load/set_items_storage"]

