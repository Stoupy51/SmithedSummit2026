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

# Custom "summit_icons" font provided by the Summit event: social-platform glyphs
# addressed by translation key. See link.py, which turns every link on a page into
# a clickable dialog button and reuses these icons.
SOCIAL_ICONS: dict[str, str] = {
	"github.com": "github",
	"smithed.dev": "smithed",
	"modrinth.com": "modrinth",
	"curseforge.com": "curseforge",
	"discord.gg": "discord",
	"discord.com": "discord",
	"youtube.com": "youtube",
	"youtu.be": "youtube",
	"twitch.tv": "twitch",
	"twitter.com": "twitter",
	"x.com": "twitter",
	"bsky.app": "bluesky",
	"instagram.com": "instagram",
	"ko-fi.com": "kofi",
	"patreon.com": "patreon",
	"planetminecraft.com": "planetminecraft",
	"mapverse": "mapverse",
}

def social_icon(key: str) -> JsonDict:
	"""A single glyph from the custom 'summit_icons' font (e.g. key='github')."""
	return {"font": "summit_icons:icons", "translate": f"summit_icons.{key}"}

def icon_for_url(url: str) -> str | None:
	"""The summit_icons key matching a URL's host, or None if we have no glyph."""
	for fragment, key in SOCIAL_ICONS.items():
		if fragment in url:
			return key
	return None

def link(label: str, url: str, color: str = "#8BE9FD") -> TextComponent:
	""" A colored, underlined link, prefixed with its platform's social icon when
	we have one. text_display entities don't fire click events in-world, so link.py
	backs every page that contains a link with an interaction entity that opens a
	dialog; there the same label is a real, clickable button (dialogs honour clicks).

	Returns a nested list component starting with an empty parent so the icon's
	custom font doesn't leak onto the label (siblings inherit from the parent)."""
	label_component: JsonDict = {
		"text": label, "color": color, "underlined": True,
		"click_event": {"action": "open_url", "url": url},
		"hover_event": {"action": "show_text", "value": f"Open {url}"},
	}
	key: str | None = icon_for_url(url)
	if key is None:
		return ["", label_component]
	return ["", social_icon(key), {"text": " "}, label_component]

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
			body("You describe "), hl("what", "gold"), body(" you want in Python. StewBeet generates everything else."),
		]),
		Page("The Problem", [
			title("The old way (2/4)\n\n"),
			body("A modern datapack means hundreds of hand-written files: models, loot tables, recipes, lang, item components...\n\n"),
			note("Tedious. Error-prone. Hard to maintain."),
		]),
		Page("The Solution", [
			title("The StewBeet way (3/4)\n\n"),
			body("Declare your items and blocks as "),
			hl("Python objects", "gold"), body(".\n\n"),
			body("Get a full "), hl("datapack"), body(" + "), hl("resource pack"),
			body(", following community conventions, for free."),
		]),
		Page("The Result", [
			title("The result (4/4)\n\n"),
			body("Focus on your "), hl("ideas", "gold"), body(", not boilerplate.\n\n"),
			body("- Fewer files\n- Fewer bugs\n- Much faster iteration"),
		]),
	]),

	# 2 Why? For Who?
	Zone("Why? For Who?", (204, 102, -23), 0, [
		Page("Modular", [
			title("Modular by design (1/4)\n\n"),
			body("StewBeet is a "), hl("pipeline"), body(" of plugins.\n\n"),
			body("Use the full suite for complete generation, or pick "), hl("only", "gold"),
			body(" the features you actually need."),
		]),
		Page("For Beginners", [
			title("Friendly for newcomers (2/4)\n\n"),
			body("Sensible defaults and ready templates: minimal, basic, extensive.\n\n"),
			code("stewbeet init basic\n\n"),
			note("Up and running in seconds."),
		]),
		Page("For Veterans", [
			title("Powerful for experts (3/4)\n\n"),
			body("Drop down to raw "), hl("beet"), body(", "), hl("bolt"),
			body(", and "), hl("mecha"), body(" whenever you want.\n\nOverride or "), hl("merge", "gold"),
			body(" any generated file."),
		]),
		Page("Battle-Tested", [
			title("Used in real projects (4/4)\n\n"),
			body("- SimplEnergy\n- LifeStealFR\n- Stardust Fragment\n- and many more\n\n"),
			note("Your next project here!"),
		]),
	]),

	# 3 Start in 3 Commands
	Zone("Start in 3 Commands", (201, 102, -20), 180, [
		Page("Install", [
			title("1. Install (1/4)\n\n"),
			code("pip install stewbeet\n\n"),
			body("Pulls in beet, bolt, mecha and all the dependencies for you."),
		]),
		Page("Create", [
			title("2. Create a project (2/4)\n\n"),
			code("stewbeet init basic\n\n"),
			body("Generates the whole project layout: beet.yml, src/, assets/, and more."),
		]),
		Page("Build", [
			title("3. Build (3/4)\n\n"),
			code("stewbeet"), note("   (or 'beet build')"), body("\n\nOutputs a ready "), hl("datapack"), body(" and "),
			hl("resource pack"), body(" zip into 'build/'."),
		]),
		Page("Auto-Copy", [
			title("Bonus: auto-copy (4/4)\n\n"),
			body("Point StewBeet at your world and resource pack folders and it copies the build there on every run:\n\n"),
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
			body("StewBeet auto-detects it and builds the model + item_model reference.\n\n"),
			note("No JSON model files by hand."),
		]),
		Page("Override the Model", [
			title("Full manual control (4/5)\n\n"),
			body("Need a custom shape? Pass a raw vanilla model dict to "), hl("override_model"),
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
			body("Placement and destruction are handled for you through "), hl("Smithed Custom Blocks"),
			body(" and optimized loops.\n\n"),
			note("No manual interaction entities."),
		]),
		Page("Ores Done Right", [
			title("One line = a real ore (3/6)\n\n"),
			body("That single "), hl("no_silk_touch_drop"),
			body(" line gives the block true ore behavior:\n\n- "), hl("Silk Touch"), body(" -> drops the block\n- otherwise -> drops your item ("),
			hl("ruby"), body(")\n- "), hl("Fortune"), body(" multiplies the count, like vanilla ores do\n\n"),
			note("Wired via Common Signals. Pass a full LootTable instead for random drops."),
		], scale=0.5, line_width=CODE_W),
		Page("Smart Ore Generation", [
			title("Ores that spawn (4/6)\n\n"),
			body("Make the ore generate in the world with "), hl("CustomOreGeneration"), body(":\n\n"),
			code("CustomOreGeneration(\n"),
			code("    dimensions=[\"minecraft:overworld\"],\n"),
			code("    maximum_height=70,\n"),
			code("    veins_per_region=4,\n"),
			code("    vein_size_logic=0.4,\n"),
			code(")\n\n"),
			note("Controls dimensions, height & vein size. Via Smart Ore Generation lib."),
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
			body("Add an "), hl("_on"), body(" texture and the block gets a powered state for free.\n\nSet "), hl("block_facing"), body(" and StewBeet builds "),
			hl("directional"), body(" variants, all recognized from names like electric_furnace_front_on.png"),
		]),
	]),

	# 6 Standing on Giants (StewBeet's dependencies)
	Zone("Standing on Giants", (194, 102, -20), 90, [
		Page("Not Reinvented", [
			title("Standing on giants (1/7)\n\n"),
			body("StewBeet did not get here alone.\n\nBehind the magic is a whole family of "),
			hl("open-source", "gold"), body(" tools, made by people who love this craft as much as you do.\n\n"),
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
			hl("mecha"), body(" compiles and type-checks every command it emits.\n\n"),
			hl("bolt"), body(" lets you script functions in real Python - loops, vars, if.\n\n"),
			link("github.com/mcbeet/beet/.../bolt", "https://github.com/mcbeet/beet/blob/main/packages/bolt/README.md"),
		], line_width=CODE_W),
		Page("Model Resolver", [
			title("Model Resolver (4/7)\n\n"),
			body("Renders every item and block to a real image, "), hl("in pure Python"),
			body(".\n\nThat is how the in-game manual shows your crafts. Thanks "), hl("@airdox", "gold"), body("!\n\n"),
			link("github.com/edayot/model_resolver", "https://github.com/edayot/model_resolver"),
		], line_width=CODE_W, scale=0.5),
		Page("The Smithed Ecosystem", [
			title("The Smithed ecosystem (5/7)\n\n"),
			hl("Crafter"), body(" for NBT recipes, "), hl("Custom Blocks"),
			body(" for placement - auto-wired.\n\nSmithed also sets shared "), hl("conventions"),
			body(" so packs stay interoperable, even in normal worlds outside the ecosystem.\n\n"),
			hl("Smithed Weld"), body(" merges your pack with its dependencies on build.\n\n"),
			link("docs.smithed.dev", "https://docs.smithed.dev/"),
		], line_width=CODE_W, scale=0.5),
		Page("Bookshelf", [
			title("Bookshelf (6/7)\n\n"),
			body("A modular toolbox of many many datapack utilities by the "), hl("Bookshelf"),
			body(" team.\n\nCall "), hl("#bs.math:..."),
			body(" in a function and StewBeet pulls in just that module.\n\n"),
			link("github.com/mcbookshelf/bookshelf", "https://github.com/mcbookshelf/bookshelf"),
		], line_width=190),
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
		Page("Recipes Live on the Item", [
			title("Recipes as objects (1/6)\n\n"),
			body("No recipe JSON. No advancement wiring. Just hand the item its recipes:\n\n"),
			code("Item(\n"),
			code("    id=\"ruby_sword\",\n"),
			code("    recipes=[CraftingShapedRecipe(\n"),
			code("        shape=[\" R \",\" R \",\" S \"],\n"),
			code("        ingredients={\n"),
			code("            \"R\": Ingr(\"ruby\"),\n"),
			code("            \"S\": Ingr(\"minecraft:stick\"),\n"),
			code("        },\n"),
			code("    )],\n"),
			code(")"),
		], line_width=CODE_W, scale=0.42),
		Page("Every Recipe Type", [
			title("One class per type (2/6)\n\n"),
			body("All the vanilla ones: "),
			hl("shaped"), body(", "), hl("shapeless"), body(", "), hl("smelting"), body(", "),
			hl("blasting"), body(", "), hl("smoking"), body(", "), hl("campfire"), body(", "),
			hl("stonecutting"), body(", "), hl("smithing"), body(".\n\nPlus custom crafters: "),
			hl("Smithed Crafter"), body(", "), hl("Furnace NBT"), body(", "),
			hl("Pulverizing"), body(", "), hl("Awakened Forge"), body("."),
		], scale=0.5, line_width=CODE_W),
		Page("Custom Items Craft Anyway", [
			title("The clever part (3/6)\n\n"),
			body("Vanilla recipes can't output NBT items, and two packs sharing them would clash.\n\nSo StewBeet quietly routes any recipe touching custom items through "), hl("Smithed"),
			body(" "), hl("Crafter"), body(" and "), hl("Furnace NBT Recipes"), body(".\n\n"),
			note("You write one recipe. It picks the engine."),
		], scale=0.5, line_width=CODE_W),
		Page("One Ingredient Helper", [
			title("Ingr, any source (4/6)\n\n"),
			code("Ingr(\"minecraft:stick\") # vanilla\n"),
			code("Ingr(\"ruby\")             # your pack\n"),
			code("Ingr(\"tin\", ns=\"mech\")  # other pack\n\n"),
			body("The same "), hl("Ingr"), body(" everywhere, it works out the item data and NBT for you. "),
			body("You can also use "), hl("Ingredient"), body(" as an alias."),
		], line_width=200, scale=0.5),
		Page("Shape the Output", [
			title("Results your way (5/6)\n\n"),
			body("The result is the item you're defining by default - but you can bend it:\n\n"),
			code("result_count=8             # bulk\n"),
			code("result=Ingr(\"bone_meal\") # other item\n"),
			code("result_count={              # random!\n"),
			code("    \"type\":\"minecraft:uniform\",\n"),
			code("    \"min\":4, \"max\":6,\n"),
			code("}\n\n"),
			note("Perfect for ore-crushing and drops."),
		], line_width=CODE_W, scale=0.45),
		Page("Loot & Manual, For Free", [
			title("The payoff (6/6)\n\n"),
			body("Every item gets a "), hl("loot table"), body(", and a "),
			hl("_give_all"), body(" function hands out chests of everything you made - great for tests.\n\nBetter yet: every recipe is "), hl("rendered", "gold"),
			body(" into the in-game manual, automatically.\n\n"),
			note("Define once. Appreciate the rest."),
		], scale=0.5),
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
			body("-> ingot, raw item, block, ore, pickaxe, axe, sword, hoe, shovel, helmet, chestplate, leggings, boots."),
		], line_width=CODE_W),
		Page("Balanced", [
			title("Tune the stats (3/3)\n\n"),
			body("Add modifiers on top of a base ore:\n\n- "), hl("attack_damage"), body("\n- "), hl("armor"), body(" / "), hl("armor_toughness"), body("\n- "), hl("mining_efficiency"), body("\n\n"),
			note("Recipes and loot come with it."),
		]),
	]),

	# 9 The Interactive In-Game Manual
	Zone("In-Game Manual", (202, 102, -25), 180, [
		Page("Free Documentation", [
			title("A manual, generated (1/3)\n\n"),
			body("StewBeet builds a full "), hl("interactive"),
			body(" manual from your items and recipes.\n\n"),
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
			body("Add an item, rebuild, and the manual updates "), hl("itself", "gold"), body(".\n\n"),
			note("Book or in-game dialog UI."),
		]),
	]),

	# 10 Quality of Life + Ecosystem
	Zone("QoL + Ecosystem", (203, 102, -28), 0, [
		Page("Auto Everything", [
			title("It writes the chores (1/6)\n\n"),
			body("- "), hl("en_us.json"), body(" lang file\n- Function "), hl("headers"), body("\n- Scoreboard "), hl("constants"), body(" detection\n\n"),
			note("Detected from your code, automatically."),
		]),
		Page("Library Magic", [
			title("Libraries, auto-wired (2/6)\n\n"),
			body("Use a Bookshelf or Smithed feature and the dependency is added for you:\n\nBookshelf, Smithed Crafter & Blocks, ItemIO, Common Signals, and more."),
		]),
		Page("Ship It", [
			title("From build to release (3/6)\n\n"),
			body("- Merge with "), hl("Smithed Weld"), body("\n- "), hl("SHA1"), body(" hashes for servers\n- Auto-copy / continuous delivery\n\n"),
			note("Ready to publish in one command."),
		]),
		Page("Compatibilities", [
			title("Plays well with others (4/6)\n\n"),
			body("Automatic special support for:\n\n- SimpleDrawer compacted drawers\n- SimplEnergy pulverizer\n- NeoEnchant veinminer"),
		]),
		Page("Get StewBeet", [
			title("Try it today (5/6)\n\n"),
			code("pip install stewbeet\n\n"),
			body("Docs:  "), hl("stewbeet.paralya.fr", "gold"), body("\nJoin the Discord community!"),
		], line_width=CODE_W),
		Page("Thank You", [
			title("Thank you! (6/6)\n\n"),
			body("Build more. Write less.\n\nPowered by "), *brand(), body("."),
		]),
	]),
]
