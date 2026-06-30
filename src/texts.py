""" Smithed Summit 2026 - StewBeet presentation walls.

10 walls (Zones), each 3x3 blocks, each with 3-6 pages navigated with arrows.
Coordinates are placeholders (0, 0, 0) and meant to be replaced in-world.

  1.  What is StewBeet?          6.  Standing on Giants (the deps)
  2.  Why? For Who?              7.  Generate Entire Material Sets
  3.  Start in 3 Commands        8.  Recipes & Loot, Automatic
  4.  Items in Pure Python       9.  The Interactive In-Game Manual
  5.  Custom Blocks Made Easy   10.  Quality of Life + Ecosystem

Note: Minecraft's font has no emoji glyphs, so the text below uses colors and
bold instead. Code snippets keep short lines to avoid wrapping on a 3x3 wall.
"""

# Imports
from dataclasses import dataclass

from stewbeet import TextComponent, create_gradient_text
from stouputils.typing import JsonDict


# https://minecraft.wiki/w/Display#Entity_data
@dataclass
class Page:
	name: str
	text: TextComponent
	line_width: int = 175
	# Per-page text size override. None = use the global PAGE_SCALE. Lower it on
	# tall pages so they don't grow up into the zone title (text is bottom-anchored,
	# so a smaller scale keeps more headroom).
	scale: float | None = None

@dataclass
class Zone:
	name: str
	coords: tuple[int, int, int]
	rotation: int
	pages: list[Page]


#  Formatting helpers
NL: JsonDict = {"text": "\n"}

def brand() -> list[JsonDict]:
	"""The 'StewBeet' wordmark as a green->red gradient."""
	return create_gradient_text("StewBeet", "#00FF00", "#FF0000")

def beet() -> list[JsonDict]:
	"""The 'Beet' wordmark as a green->red gradient."""
	return create_gradient_text("Beet", "#00C400", "#FF0000")

def title(text: str) -> JsonDict:
	return {"text": text, "bold": True, "color": "gold"}

def body(text: str, color: str = "white") -> JsonDict:
	return {"text": text, "color": color}

def hl(text: str, color: str = "aqua") -> JsonDict:
	"""An inline highlighted word."""
	return {"text": text, "bold": True, "color": color}

def code(text: str) -> JsonDict:
	return {"text": text, "color": "#8BE9FD"}

def note(text: str) -> JsonDict:
	return {"text": text, "color": "#7F8C99", "italic": True}

def link(label: str, url: str, color: str = "#8BE9FD") -> JsonDict:
	"""A colored, underlined link. text_display entities don't fire click events
	in-world, so the label doubles as a human-readable URL; the click/hover are
	kept for any context (chat echo, future dialogs) that does honour them."""
	return {
		"text": label, "color": color, "underlined": True,
		"click_event": {"action": "open_url", "url": url},
		"hover_event": {"action": "show_text", "value": f"Open {url}"},
	}

# Wider wrap so short code lines are never re-wrapped.
CODE_W: int = 220

#  The walls
TEXTS: list[Zone] = [

	# 1 What is StewBeet?
	Zone("What is StewBeet?", (211, 102, -19), 90, [
		Page("Introduction", [
			title("Introduction (1/4)\n\n"),
			body("It is a "), beet(), body(" framework that brings huge "),
			hl("automation"), body(" to Minecraft datapacks.\n\n"),
			body("You describe "), hl("what", "gold"), body(" you want in Python. "),
			body("StewBeet generates everything else."),
		]),
		Page("The Problem", [
			title("The old way (2/4)\n\n"),
			body("A modern datapack means hundreds of hand-written files: models, loot tables, "),
			body("recipes, lang, item components...\n\n"),
			note("Tedious. Error-prone.\nHard to maintain."),
		]),
		Page("The Solution", [
			title("The StewBeet way (3/4)\n\n"),
			body("Declare your items and blocks as\n"),
			hl("Python objects", "gold"), body(".\n\n"),
			body("Get a full "), hl("datapack"), body(" + "), hl("resource pack"),
			body(", following community conventions, for free."),
		]),
		Page("The Result", [
			title("The result (4/4)\n\n"),
			body("Focus on your "), hl("ideas", "gold"), body(", not boilerplate.\n\n"),
			body("- Fewer files\n"),
			body("- Fewer bugs\n"),
			body("- Much faster iteration"),
		]),
	]),

	# 2 Why? For Who?
	Zone("Why? For Who?", (204, 102, -23), 0, [
		Page("Modular", [
			title("Modular by design (1/4)\n\n"),
			body("StewBeet is a "), hl("pipeline"), body(" of plugins.\n\n"),
			body("Use the full suite for complete "),
			body("generation, or pick "), hl("only", "gold"),
			body(" the features you actually need."),
		]),
		Page("For Beginners", [
			title("Friendly for newcomers (2/4)\n\n"),
			body("Sensible defaults and ready templates: "),
			body("minimal, basic, extensive.\n\n"),
			code("stewbeet init basic\n\n"),
			note("Up and running in seconds."),
		]),
		Page("For Veterans", [
			title("Powerful for experts (3/4)\n\n"),
			body("Drop down to raw "), hl("beet"), body(", "), hl("bolt"),
			body(", and "), hl("mecha"), body(" whenever you want.\n\n"),
			body("Override or "), hl("merge", "gold"),
			body(" any generated file."),
		]),
		Page("Battle-Tested", [
			title("Used in real projects (4/4)\n\n"),
			body("- SimplEnergy\n"),
			body("- LifeStealFR\n"),
			body("- Stardust Fragment\n"),
			body("- and many more\n\n"),
			note("Your next project here!"),
		]),
	]),

	# 3 Start in 3 Commands
	Zone("Start in 3 Commands", (201, 102, -20), 180, [
		Page("Install", [
			title("1. Install (1/4)\n\n"),
			code("pip install stewbeet\n\n"),
			body("Pulls in beet, bolt, mecha and all\n"),
			body("the dependencies for you."),
		]),
		Page("Create", [
			title("2. Create a project (2/4)\n\n"),
			code("stewbeet init basic\n\n"),
			body("Generates the whole project layout: "),
			body("beet.yml, src/, assets/, and more."),
		]),
		Page("Build", [
			title("3. Build (3/4)\n\n"),
			code("stewbeet\n\n"),
			body("Outputs a ready "), hl("datapack"), body(" and\n"),
			hl("resource pack"), body(" zip into 'build/'."),
		]),
		Page("Auto-Copy", [
			title("Bonus: auto-copy (4/4)\n\n"),
			body("Point StewBeet at your world and resource pack folders and it "),
			body("copies the build there on every run:\n\n"),
			code("build_copy_destinations:\n"),
			code("  datapack: \n   - \".../datapacks\",\n   - \"sftp://user:pass@host/path\"\n\n"),
			code("  resource_pack: \n   - \"D:/minecraft/latest/resourcepacks\"\n\n"),
			body("(Works over SFTP too and password can be moved to a credentials file)"),
		], scale=0.4, line_width=CODE_W),
	]),

	# 4 Items in Pure Python
	Zone("Items in Pure Python", (196, 102, -12), 180, [
		Page("The Item Class", [
			title("Define an item (1/4)\n\n"),
			code("Item(\n"),
			code("    id=\"ruby\",\n"),
			code("    base_item=\"minecraft:diamond\",\n"),
			code("    components={\n"),
			code("        \"lore\": [{\"text\": \"Shiny!\"}],\n"),
			code("    },\n"),
			code(")"),
		], line_width=CODE_W),
		Page("Components", [
			title("Vanilla components (2/4)\n\n"),
			body("Use any item component, without the\n"),
			hl("minecraft:"), body(" prefix:\n\n"),
			code("\"enchantments\": {\n"),
			code("    \"minecraft:sharpness\": 5\n"),
			code("},\n"),
			code("\"max_damage\": 500"),
		], line_width=CODE_W),
		Page("Textures Are Automatic", [
			title("Just drop a texture (3/4)\n\n"),
			body("Put "), hl("ruby.png"), body(" in assets/textures/\n\n"),
			body("StewBeet auto-detects it and builds\n"),
			body("the model + item_model reference.\n\n"),
			note("No JSON model files by hand."),
		]),
		Page("Access Anywhere", [
			title("One global registry (4/4)\n\n"),
			body("Every definition lives in "), hl("Mem.definitions"),
			body(".\n\n"),
			code("ruby = Item.from_id(\"ruby\")\n"),
			code("ruby.manual_category = \"materials\""),
		], line_width=CODE_W),
	]),

	# 5 Custom Blocks Made Easy
	Zone("Custom Blocks Made Easy", (191, 102, -17), -90, [
		Page("The Block Class", [
			title("Define a block (1/4)\n\n"),
			code("Block(\n"),
			code("    id=\"ruby_ore\",\n"),
			code("    vanilla_block=VanillaBlock(\n"),
			code("        id=\"minecraft:stone\",\n"),
			code("    ),\n"),
			code("    no_silk_touch_drop=\"ruby\",\n"),
			code(")"),
		], line_width=CODE_W),
		Page("Placement & Breaking", [
			title("It just works (2/4)\n\n"),
			body("Placement and destruction are handled\n"),
			body("for you through "), hl("Smithed Custom Blocks"),
			body(".\n\n"),
			note("No manual interaction entities."),
		]),
		Page("Ores Done Right", [
			title("Ores out of the box (3/4)\n\n"),
			body("- "), hl("Silk touch"), body(" drops the block\n"),
			body("- "), hl("Fortune"), body(" multiplies the drops\n"),
			body("- Custom no-silk-touch drops\n\n"),
			note("Plus Smart Ore Generation support."),
		]),
		Page("States & Facing", [
			title("Smart model detection (4/4)\n\n"),
			body("Name your textures and StewBeet picks\n"),
			body("the right model: "), hl("on/off"), body(" states and\n"),
			hl("directional"), body(" facing, recognized from\n"),
			body("names like furnace_front_on.png."),
		]),
	]),

	# 6 Standing on Giants (StewBeet's dependencies)
	Zone("Standing on Giants", (197, 102, -28), 0, [
		Page("Not Reinvented", [
			title("Standing on giants (1/6)\n\n"),
			body("StewBeet generates datapacks, but it\n"),
			body("never parses Minecraft on its own.\n\n"),
			body("It orchestrates a proven, open-source\n"),
			hl("Python toolchain"), body(" underneath."),
		]),
		Page("beet", [
			title("beet - the foundation (2/6)\n\n"),
			body("The pack dev kit by "), hl("Valentin Berlier", "gold"),
			body(".\nProjects, the build "), hl("pipeline"), body(", and the\n"),
			body("data + resource pack model itself.\n\n"),
			link("github.com/mcbeet/beet", "https://github.com/mcbeet/beet"),
		], line_width=CODE_W),
		Page("mecha + bolt", [
			title("mecha + bolt (3/6)\n\n"),
			hl("mecha"), body(" compiles and type-checks\n"),
			body("every command it emits.\n\n"),
			hl("bolt"), body(" lets you script functions in\n"),
			body("real Python - loops, vars, if.\n\n"),
			link("github.com/mcbeet/bolt", "https://github.com/mcbeet/bolt"),
		], line_width=CODE_W),
		Page("Model Resolver", [
			title("Model Resolver (4/6)\n\n"),
			body("Renders every item and block to a\n"),
			body("real image, "), hl("in pure Python"), body(".\n\n"),
			body("That is how the in-game manual shows\n"),
			body("your crafts. Thanks "), hl("@edayot", "gold"), body("!\n\n"),
			link("github.com/edayot/model_resolver", "https://github.com/edayot/model_resolver"),
		], line_width=CODE_W),
		Page("The Smithed Ecosystem", [
			title("The Smithed ecosystem (5/6)\n\n"),
			body("Community libraries, auto-wired:\n"),
			body("Crafter, Custom Blocks, Bookshelf...\n\n"),
			hl("Smithed Weld"), body(" then merges your pack\n"),
			body("with its dependencies on build.\n\n"),
			link("weld.smithed.dev", "https://weld.smithed.dev/"),
		], line_width=CODE_W),
		Page("And the Glue", [
			title("...and the glue (6/6)\n\n"),
			hl("stouputils"), body(" - logging & helpers\n"),
			hl("paramiko / fsspec"), body(" - SFTP deploy\n"),
			hl("mutagen"), body(" - music disc metadata\n\n"),
			note("Open source, all the way down."),
		]),
	]),

	# 7 Generate Entire Material Sets
	Zone("Generate Material Sets", (194, 102, -20), 90, [
		Page("One Config", [
			title("Describe a material once (1/3)\n\n"),
			code("ORES_CONFIGS = {\n"),
			code("  \"ruby\": EquipmentsConfig(\n"),
			code("    equivalent_to=DefaultOre.DIAMOND,\n"),
			code("    attributes={\"attack_damage\": 1},\n"),
			code("  ),\n"),
			code("}"),
		], line_width=CODE_W),
		Page("Generate Everything", [
			title("One call, a whole set (2/3)\n\n"),
			code("generate_everything_about_\n"),
			code("these_materials(ORES_CONFIGS)\n\n"),
			body("-> ingot, raw item, block, ore,\n"),
			body("pickaxe, axe, sword, hoe, shovel,\n"),
			body("helmet, chestplate, leggings, boots."),
		], line_width=CODE_W),
		Page("Balanced", [
			title("Tune the stats (3/3)\n\n"),
			body("Add modifiers on top of a base ore:\n\n"),
			body("- "), hl("attack_damage"), body("\n"),
			body("- "), hl("armor"), body(" / "), hl("armor_toughness"), body("\n"),
			body("- "), hl("mining_efficiency"), body("\n\n"),
			note("Recipes and loot come with it."),
		]),
	]),

	# 8 Recipes & Loot, Automatic
	Zone("Recipes & Loot", (191, 102, -23), -90, [
		Page("Typed Recipes", [
			title("Recipes as objects (1/4)\n\n"),
			code("CraftingShapedRecipe(\n"),
			code("    shape=[\"XX\", \"XX\"],\n"),
			code("    ingredients={\n"),
			code("        \"X\": Ingr(\"ruby\"),\n"),
			code("    },\n"),
			code(")"),
		], line_width=CODE_W),
		Page("Every Recipe Type", [
			title("All the types (2/4)\n\n"),
			body("Shaped, shapeless, smelting, blasting,\n"),
			body("smoking, campfire, stonecutting,\n"),
			body("smithing - plus "), hl("Smithed Crafter"), body(" and\n"),
			hl("Furnace NBT"), body(" recipes."),
		]),
		Page("Free Loot Tables", [
			title("Loot for every item (3/4)\n\n"),
			body("Each definition gets a loot table, and\n"),
			body("a "), hl("_give_all"), body(" function hands out named\n"),
			body("chests of everything you made.\n\n"),
			note("Great for testing in-world."),
		]),
		Page("Ingredients", [
			title("The Ingr helper (4/4)\n\n"),
			code("Ingr(\"ruby\")          # your item\n"),
			code("Ingr(\"minecraft:stick\") # vanilla\n"),
			code("Ingr(\"tin\", ns=\"mech\")  # other pack\n\n"),
			note("One helper for every source."),
		], line_width=CODE_W),
	]),

	# 9 The Interactive In-Game Manual
	Zone("In-Game Manual", (202, 102, -25), 180, [
		Page("Free Documentation", [
			title("A manual, generated (1/3)\n\n"),
			body("StewBeet builds a full "), hl("interactive"),
			body("\nmanual from your items and recipes.\n\n"),
			note("Every recipe, rendered and clickable."),
		]),
		Page("Wiki Buttons", [
			title("Add your own notes (2/3)\n\n"),
			code("Item.from_id(\"ruby\").wiki_buttons = [\n"),
			code("    WikiButton({\n"),
			code("        \"text\": \"Drops from Ruby Ore\",\n"),
			code("    }),\n"),
			code("]"),
		], line_width=CODE_W),
		Page("Always Up To Date", [
			title("Never stale (3/3)\n\n"),
			body("Add an item, rebuild, and the manual\n"),
			body("updates "), hl("itself", "gold"), body(".\n\n"),
			note("Book or in-game dialog UI."),
		]),
	]),

	# 10 Quality of Life + Ecosystem
	Zone("QoL + Ecosystem", (203, 102, -28), 0, [
		Page("Auto Everything", [
			title("It writes the chores (1/6)\n\n"),
			body("- "), hl("en_us.json"), body(" lang file\n"),
			body("- Function "), hl("headers"), body("\n"),
			body("- Scoreboard "), hl("constants"), body(" detection\n\n"),
			note("Detected from your code, automatically."),
		]),
		Page("Library Magic", [
			title("Libraries, auto-wired (2/6)\n\n"),
			body("Use a Bookshelf or Smithed feature and\n"),
			body("the dependency is added for you:\n\n"),
			body("Bookshelf, Smithed Crafter & Blocks,\n"),
			body("ItemIO, Common Signals, and more."),
		]),
		Page("Ship It", [
			title("From build to release (3/6)\n\n"),
			body("- Merge with "), hl("Smithed Weld"), body("\n"),
			body("- "), hl("SHA1"), body(" hashes for servers\n"),
			body("- Auto-copy / continuous delivery\n\n"),
			note("Ready to publish in one command."),
		]),
		Page("Compatibilities", [
			title("Plays well with others (4/6)\n\n"),
			body("Automatic special support for:\n\n"),
			body("- SimpleDrawer compacted drawers\n"),
			body("- SimplEnergy pulverizer\n"),
			body("- NeoEnchant veinminer"),
		]),
		Page("Get StewBeet", [
			title("Try it today (5/6)\n\n"),
			code("pip install stewbeet\n\n"),
			body("Docs:  "), hl("stewbeet.paralya.fr", "gold"), body("\n"),
			body("Join the Discord community!"),
		], line_width=CODE_W),
		Page("Thank You", [
			title("Thank you! (6/6)\n\n"),
			body("Build more. Write less.\n\n"),
			body("Powered by "), *brand(), body("."),
		]),
	]),
]

