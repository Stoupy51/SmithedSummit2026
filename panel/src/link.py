
# Imports
from stewbeet import *  # type: ignore


def beet_default(ctx: Context) -> None:
	ns: str = Mem.ctx.project_id

	# Meow
	write_function(f"{ns}:uwu", f"""
say {ns}.uwu
""")

