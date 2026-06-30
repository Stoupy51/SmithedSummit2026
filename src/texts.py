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
	""" A colored, underlined link. text_display entities don't fire click events
	in-world, so the label doubles as a human-readable URL; the click/hover are
	kept for any context (chat echo, future dialogs) that does honour them."""
	# TODO: Add an interaction entity that opens a single dialog with the URL
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
			title("Define an item (1/5)\n\n"),
			body("Here is a very simple item definition:\n\n"),
			code("Item(\n"),
			code("    id=\"ruby\",\n"),
			code("    base_item=\"minecraft:diamond\",\n"),
			code("    components={\n"),
			code("        \"lore\": [{\"text\": \"Shiny!\"}],\n"),
			code("    },\n"),
			code(")"),
		], scale=0.55),
		Page("Components", [
			title("Vanilla components (2/5)\n\n"),
			body("Use or remove any item component like you would in a JSON file:\n\n"),
			code("{\n"),
			code("    \"enchantments\": {\n"),
			code("        \"minecraft:sharpness\": 5\n"),
			code("    },\n"),
			code("    \"max_damage\": 500,\n"),
			code("    !repairable: {}\n"),
			code("}"),
		], line_width=CODE_W, scale=0.5),
		Page("Textures Are Automatic", [
			title("Just drop a texture (3/5)\n\n"),
			body("Put "), hl("ruby.png"), body(" in assets/textures/\n\n"),
			body("StewBeet auto-detects it and builds "),
			body("the model + item_model reference.\n\n"),
			note("No JSON model files by hand."),
		]),
		Page("Override the Model", [
			title("Full manual control (4/5)\n\n"),
			body("Need a custom shape? Pass a raw\n"),
			body("vanilla model dict to "), hl("override_model"),
			body(":\n\n"),
			code("Item(\n"),
			code("    id=\"black_hole\",\n"),
			code("    override_model={\n"),
			code("        \"textures\": {...},\n"),
			code("        \"elements\": [...],\n"),
			code("    },\n"),
			code(")\n\n"),
			note("Auto-detection off: you own the model."),
		], line_width=CODE_W, scale=0.45),
		Page("Access Anywhere", [
			title("One global registry (5/5)\n\n"),
			body("Every definition lives in "), hl("Mem.definitions"),
			body(". You can access it from anywhere and update it.\n\n"),
			code("ruby = Item.from_id(\"ruby\")\n"),
			code("ruby.manual_category = \"materials\""),
		], line_width=200),
	]),

	# 5 Custom Blocks Made Easy
	Zone("Custom Blocks\nMade Easy", (191, 102, -17), -90, [
		Page("The Block Class", [
			title("Define a block (1/6)\n\n"),
			code("Block(\n"),
			code("    id=\"ruby_ore\",\n"),
			code("    vanilla_block=VanillaBlock(\n"),
			code("        id=\"minecraft:stone\",\n"),
			code("    ),\n"),
			code("    no_silk_touch_drop=\"ruby\",\n"),
			code(")"),
		], line_width=CODE_W),
		Page("Placement & Breaking", [
			title("It just works (2/6)\n\n"),
			body("Placement and destruction are handled "),
			body("for you through "), hl("Smithed Custom Blocks"),
			body(" and optimized loops.\n\n"),
			note("No manual interaction entities."),
		]),
		Page("Ores Done Right", [
			title("One line = a real ore (3/6)\n\n"),
			body("That single "), hl("no_silk_touch_drop"),
			body(" line gives the block true ore behavior:\n\n"),
			body("- "), hl("Silk Touch"), body(" -> drops the block\n"),
			body("- otherwise -> drops your item ("), hl("ruby"), body(")\n"),
			body("- "), hl("Fortune"), body(" multiplies the count, like\n  vanilla ores do\n\n"),
			note("Wired via Common Signals. Pass a full LootTable instead for random drops."),
		], scale=0.5, line_width=CODE_W),
		Page("Smart Ore Generation", [
			title("Ores that spawn (4/6)\n\n"),
			body("Make the ore generate in the world\n"),
			body("with "), hl("CustomOreGeneration"), body(":\n\n"),
			code("CustomOreGeneration(\n"),
			code("    dimensions=[\"minecraft:overworld\"],\n"),
			code("    maximum_height=70,\n"),
			code("    veins_per_region=4,\n"),
			code("    vein_size_logic=0.4,\n"),
			code(")\n\n"),
			note("Controls dimensions, height & vein size.\nVia Smart Ore Generation lib."),
		], scale=0.45, line_width=CODE_W),
		Page("Texture Patterns", [
			title("Texture name patterns (5/6)\n\n"),
			body("StewBeet tries to auto-detect the textures for you and check for patterns:\n\n"),
			hl("front+side+top+bottom"), body(" -> furnace\n"),
			hl("bottom+side+top"), body(" -> barrel\n"),
			hl("end+side"), body(" -> pillar\n"),
			hl("bottom+side+top+inner"), body(" -> cake\n\n"),
			note("One texture -> cube_all."),
		], scale=0.5, line_width=CODE_W),
		Page("States & Facing", [
			title("States & facing (6/6)\n\n"),
			body("Add an "), hl("_on"), body(" texture and the block\n"),
			body("gets a powered state for free.\n\n"),
			body("Set "), hl("block_facing"), body(" and StewBeet builds "),
			hl("directional"), body(" variants, all recognized "),
			body("from names like electric_furnace_front_on.png"),
		]),
	]),

	# 6 Standing on Giants (StewBeet's dependencies)
	Zone("Standing on Giants", (194, 102, -20), 90, [
		Page("Not Reinvented", [
			title("Standing on giants (1/7)\n\n"),
			body("StewBeet did not get here alone.\n\n"),
			body("Behind the magic is a whole family of "),
			hl("open-source", "gold"), body(" tools, made by people "),
			body("who love this craft as much as you do.\n\n"),
			note("The next pages are a thank-you."),
		]),
		Page("beet", [
			title("beet - the foundation (2/7)\n\n"),
			body("The beet project is a development kit that tries to "), hl("unify"),
			body(" data pack and resource pack tooling into a single "), hl("pipeline"),
			body(".\n\n"),
			link("github.com/mcbeet/beet", "https://github.com/mcbeet/beet"),
		]),
		Page("mecha + bolt", [
			title("mecha + bolt (3/7)\n\n"),
			hl("mecha"), body(" compiles and type-checks\n"),
			body("every command it emits.\n\n"),
			hl("bolt"), body(" lets you script functions in\n"),
			body("real Python - loops, vars, if.\n\n"),
			link("github.com/mcbeet/beet/.../bolt", "https://github.com/mcbeet/beet/blob/main/packages/bolt/README.md"),
		], line_width=CODE_W),
		Page("Model Resolver", [
			title("Model Resolver (4/7)\n\n"),
			body("Renders every item and block to a "),
			body("real image, "), hl("in pure Python"), body(".\n\n"),
			body("That is how the in-game manual shows "),
			body("your crafts. Thanks "), hl("@airdox", "gold"), body("!\n\n"),
			link("github.com/edayot/model_resolver", "https://github.com/edayot/model_resolver"),
		], line_width=CODE_W, scale=0.5),
		Page("The Smithed Ecosystem", [
			title("The Smithed ecosystem (5/7)\n\n"),
			hl("Crafter"), body(" for NBT recipes, "), hl("Custom Blocks"),
			body(" for placement - auto-wired.\n\n"),
			body("Smithed also sets shared "), hl("conventions"),
			body(" so packs stay interoperable, even in\n"),
			body("normal worlds outside the ecosystem.\n\n"),
			hl("Smithed Weld"), body(" merges your pack with "),
			body("its dependencies on build.\n\n"),
			link("docs.smithed.dev", "https://docs.smithed.dev/"),
		], line_width=CODE_W, scale=0.5),
		Page("Bookshelf", [
			title("Bookshelf (6/7)\n\n"),
			body("A modular toolbox of many many datapack "),
			body("utilities by the "), hl("Bookshelf"), body(" team.\n\n"),
			body("Call "), hl("#bs.math:..."), body(" in a function and "),
			body("StewBeet pulls in just that module.\n\n"),
			link("github.com/mcbookshelf/bookshelf", "https://github.com/mcbookshelf/bookshelf"),
		]),
		Page("More Libraries", [
			title("...and more libraries (7/7)\n\n"),
			body("Each pulled in automatically only when a function references it:\n\n"),
			hl("Furnace NBT Recipes"), body(" - furnaces\n"),
			hl("Common Signals"), body(" - event hooks\n"),
			hl("ItemIO"), body(" - item transport\n"),
			hl("Realistic Explosion"), body(" - blasts\n"),
			hl("Smithed Actionbar"), body(" - action bar\n"),
			hl("Player Motion"), body(" - movement\n"),
			note("...and more!"),
		], scale=0.5, line_width=CODE_W),
	]),

	# 7 Recipes & Loot, Automatic
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

	# 8 Generate Entire Material Sets
	Zone("Generate Material Sets", (197, 102, -28), 0, [
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

