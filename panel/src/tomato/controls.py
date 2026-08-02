""" Stage controls for the tomatoes.

Every command here is unversioned on purpose, so they stay short enough to type live:
`/function stoupy_panel:tomato/give`, `/enable`, `/disable` and `/clear`.
"""
# Imports
from beet import ItemModifier
from stewbeet import Mem, write_function, write_load_file, write_versioned_function

from .constants import ENABLED_SCORE, TOMATO_ITEM, TOMATO_TAG, TOMATOES_PER_PLAYER

# Constants
ITEMS_LOOT_FOLDER: str = "i"
""" Folder StewBeet writes the per item loot tables into. """


# Classes
class TomatoControls:
	""" Give, arm, disarm and clean up the tomatoes. """

	@staticmethod
	def write_setup() -> None:
		""" Declare the objectives and start the panel with the tomatoes disarmed. """
		ns: str = Mem.ctx.project_id

		write_load_file(f"""
scoreboard objectives add {ns}.data dummy
scoreboard objectives add {ns}.{TOMATO_ITEM}.life dummy
scoreboard players set {ENABLED_SCORE} {ns}.data 0
""")

		# Spending one tomato per throw, so a stack is a real budget
		Mem.ctx.data[ns].item_modifiers[f"v{Mem.ctx.project_version}/{TOMATO_ITEM}/consume_one"] = ItemModifier(
			[{"function": "minecraft:set_count", "count": -1, "add": True}]
		)

	@staticmethod
	def write_commands() -> None:
		""" Write the four functions used from the stage. """
		ns: str = Mem.ctx.project_id
		version: str = Mem.ctx.project_version

		give_lines: str = "\n".join(
			f"loot give @a[gamemode=!spectator] loot {ns}:{ITEMS_LOOT_FOLDER}/{TOMATO_ITEM}"
			for _ in range(TOMATOES_PER_PLAYER)
		)
		write_versioned_function(f"{TOMATO_ITEM}/give", f"""
{give_lines}
tellraw @a [{{"text": "You got {TOMATOES_PER_PLAYER} tomatoes. ", "color": "red"}}, {{"text": "Right click to throw them at me.", "color": "gray"}}]
playsound minecraft:entity.item.pickup master @a ~ ~ ~ 1 1.2
""")

		write_versioned_function(f"{TOMATO_ITEM}/enable", f"""
scoreboard players set {ENABLED_SCORE} {ns}.data 1
tellraw @a {{"text": "Tomatoes are live!", "color": "red", "bold": true}}
""")

		write_versioned_function(f"{TOMATO_ITEM}/disable", f"""
scoreboard players set {ENABLED_SCORE} {ns}.data 0
function {ns}:v{version}/{TOMATO_ITEM}/clear
tellraw @a {{"text": "That is enough tomatoes, thank you.", "color": "gray", "italic": true}}
""")

		# Wipes what is currently in the air, without taking back what people still hold
		write_versioned_function(f"{TOMATO_ITEM}/clear", f"""
execute as @e[type=item_display, tag={ns}.{TOMATO_TAG}] at @s run function {ns}:v{version}/{TOMATO_ITEM}/splat
""")

		# Short aliases, because typing a version number on stage is a bad idea
		for command in ("give", "enable", "disable", "clear"):
			write_function(f"{ns}:{TOMATO_ITEM}/{command}", f"function {ns}:v{version}/{TOMATO_ITEM}/{command}")

	@staticmethod
	def write() -> None:
		""" Write the setup and every stage control. """
		TomatoControls.write_setup()
		TomatoControls.write_commands()
