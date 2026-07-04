""" The presentation-wall content: Page/Zone dataclasses and the TEXTS list.

10 walls (Zones), each a 3x3 block face with 3-9 pages navigated with arrows.
Coordinates are the in-world anchor block of each wall.

  1.  What is StewBeet?          6.  Standing on Giants (the deps)
  2.  Why? For Who?              7.  Recipes & Loot, Automatic
  3.  Start in 3 Commands        8.  Generate Entire Material Sets
  4.  Items in Pure Python       9.  The Interactive In-Game Manual
  5.  Custom Blocks Made Easy   10.  Quality of Life + Ecosystem

Edit the copy here. builder.py turns each Zone into display entities and a set of
per-page functions; format.py provides the text stylers and links.py the link().
Code snippets keep short lines to avoid wrapping on a 3x3 wall.
"""

# Imports
from dataclasses import dataclass

from stewbeet import TextComponent

from .format import beet, body, brand, cmd, code, hl, note, title
from .links import link


# https://minecraft.wiki/w/Display#Entity_data
@dataclass
class Page:
	""" One page of a wall: a named text component plus its display tuning. """
	name: str
	""" Page title, shown as the subtitle of the click-to-open link dialog. """
	text: TextComponent
	""" The page body, as a list of text components (see format.py stylers). """
	line_width: int = 175
	""" text_display wrapping width; raise it (e.g. CODE_W) so code lines never re-wrap. """
	scale: float | None = None
	""" Per-page text size override. None = use the global PAGE_SCALE. Lower it on
	tall pages so they don't grow up into the zone title (text is bottom-anchored,
	so a smaller scale keeps more headroom). """
	sticker: str | None = None
	""" Sticker id (see booth.json) rewarded to the player who navigates onto this
	page, via the summit.sticker_book:<ns>/<sticker_id> advancement (see
	navigation.py). Reaching it needs no click. """

@dataclass
class Zone:
	""" One presentation wall: its title, in-world anchor and pages. """
	name: str
	""" Wall title, floated above the wall (and used to derive the function folder slug). """
	coords: tuple[int, int, int]
	""" In-world anchor block of the wall. """
	rotation: int
	""" Yaw the wall faces; flip by 180 if its text/arrows face the wrong way. """
	pages: list[Page]
	""" The pages navigated with the arrows, in order. """


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
			brand(), body(" generates everything else.\n\n"),
			link("stewbeet.paralya.fr", r"https://stewbeet.paralya.fr"), body("\n"),
			link("discord.gg/anxzu6rA9F", r"https://discord.gg/anxzu6rA9F"), body("\n"),
			link("Made by Stoupy", r"https://github.com/Stoupy51/StewBeet"),
		], scale=0.55),
		Page("The Problem", [
			title("The old way (2/4)\n\n"),
			body("A modern datapack means hundreds of hand-written files: models, loot tables, recipes, lang, item components...\n\n"),
			note("Tedious. Error-prone. Hard to maintain."),
		]),
		Page("The Solution", [
			title("The "), brand(), title(" way (3/4)\n\n"),
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
			brand(), body(" is a "), hl("pipeline"), body(" of plugins.\n\n"),
			body("Use the full suite for complete generation, or pick "), hl("only", "gold"),
			body(" the features you actually need."),
		]),
		Page("For Beginners", [
			title("Friendly for newcomers (2/4)\n\n"),
			body("Sensible defaults and ready templates: minimal, basic, extensive.\n\n"),
			cmd("stewbeet init basic\n\n"),
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
			cmd("pip install stewbeet\n\n"),
			body("Pulls in beet, bolt, mecha and all the dependencies for you.\n\n"),
			link("Docs: Getting Started", r"https://stewbeet.paralya.fr/markdown?src=0_getting_started%2Fen.md"),
		]),
		Page("Create", [
			title("2. Create a project (2/4)\n\n"),
			cmd("stewbeet init basic\n\n"),
			body("Generates the whole project layout: beet.yml, src/, assets/, and more."),
		]),
		Page("Build", [
			title("3. Build (3/4)\n\n"),
			cmd("stewbeet"), note("   (or 'beet build')"), body("\n\nOutputs a ready "), hl("datapack"), body(" and "),
			hl("resource pack"), body(" zip into 'build/'."),
		]),
		Page("Auto-Copy", [
			title("Bonus: auto-copy (4/4)\n\n"),
			body("Point "), brand(), body(" at your world and resource pack folders and it copies the build there on every run:\n\n"),
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
			code("    \"!repairable\": {},\n"),
			code("}"),
		], line_width=CODE_W, scale=0.5),
		Page("Textures Are Automatic", [
			title("Just drop a texture (3/5)\n\n"),
			body("Put "), hl("ruby.png"), body(" in assets/textures/\n\n"),
			brand(), body(" auto-detects it and builds the model + item_model reference.\n\n"),
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
			code("ruby.manual_category = \"materials\"\n\n"),
			link("Docs: Definitions Setup", r"https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"),
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
			note("Controls dimensions, height & vein size.\nVia Smart Ore Generation lib."),
		], scale=0.45, line_width=CODE_W),
		Page("Texture Patterns", [
			title("Texture name patterns (5/6)\n\n"),
			brand(), body(" tries to auto-detect the textures for you and check for patterns:\n\n"),
			hl("front+side+top+bottom"), body(" -> furnace\n"),
			hl("bottom+side+top"), body(" -> barrel\n"),
			hl("end+side"), body(" -> pillar\n"),
			hl("bottom+side+top+inner"), body(" -> cake\n\n"),
			note("One texture -> cube_all."),
		], scale=0.5, line_width=CODE_W),
		Page("States & Facing", [
			title("States & facing (6/6)\n\n"),
			body("Add an "), hl("_on"), body(" texture and the block gets a powered state for free.\n\nSet "), hl("block_facing"), body(" and "), brand(), body(" builds "),
			hl("directional"), body(" variants, all recognized from names like electric_furnace_front_on.png\n\n"),
			link("Docs: Definitions Setup", r"https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"),
		]),
	]),

	# 6 Standing on Giants (StewBeet's dependencies)
	Zone("Standing on Giants", (194, 102, -20), 90, [
		Page("Not Reinvented", [
			title("Standing on giants (1/7)\n\n"),
			brand(), body(" did not get here alone.\n\nBehind the magic is a whole family of "),
			hl("open-source", "gold"), body(" tools, made by people who love this craft as much as you do.\n\n"),
			note("The next pages are a thank-you."),
		]),
		Page("beet", [
			title("beet - the foundation (2/7)\n\n"),
			body("The beet project is a development kit that tries to "), hl("unify"),
			body(" data pack and resource pack tooling into a single "), hl("pipeline"),
			body(".\n\n"),
			link("github.com/mcbeet/beet", r"https://github.com/mcbeet/beet"),
		]),
		Page("mecha + bolt", [
			title("mecha + bolt (3/7)\n\n"),
			hl("mecha"), body(" compiles and type-checks every command it emits.\n\n"),
			hl("bolt"), body(" lets you script functions in real Python - loops, vars, if.\n\n"),
			link("github.com/mcbeet/beet/.../bolt", r"https://github.com/mcbeet/beet/blob/main/packages/bolt/README.md"),
		], line_width=CODE_W, scale=0.5),
		Page("Model Resolver", [
			title("Model Resolver (4/7)\n\n"),
			body("Renders every item and block to a real image, "), hl("in pure Python"),
			body(".\n\nThat is how the in-game manual shows your crafts. Thanks "), hl("@airdox", "gold"), body("!\n\n"),
			link("github.com/edayot/model_resolver", r"https://github.com/edayot/model_resolver"),
		], line_width=CODE_W, scale=0.5),
		Page("The Smithed Ecosystem", [
			title("The Smithed ecosystem (5/7)\n\n"),
			hl("Crafter"), body(" for NBT recipes, "), hl("Custom Blocks"),
			body(" for placement - auto-wired.\n\nSmithed also sets shared "), hl("conventions"),
			body(" so packs stay interoperable, even in normal worlds outside the ecosystem.\n\n"),
			hl("Smithed Weld"), body(" merges your pack with its dependencies on build.\n\n"),
			link("docs.smithed.dev", r"https://docs.smithed.dev/"),
		], line_width=CODE_W, scale=0.5),
		Page("Bookshelf", [
			title("Bookshelf (6/7)\n\n"),
			body("A modular toolbox of many many datapack utilities by the "), hl("Bookshelf"),
			body(" team.\n\nCall "), hl("#bs,math:..."),
			body(" in a function and "), brand(), body(" pulls in just that module.\n\n"),
			link("github.com/mcbookshelf/bookshelf", r"https://github.com/mcbookshelf/bookshelf"),
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
			note("...and more!\n\n"),
			link("Docs: Libraries Support", r"https://stewbeet.paralya.fr/markdown?src=5_dependencies%2Fen.md"),
		], scale=0.475, line_width=CODE_W),
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
			body("Vanilla recipes can't output NBT items, and two packs sharing them would clash.\n\nSo "), brand(), body(" quietly routes any recipe touching custom items through "), hl("Smithed"),
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
			code("    \"type\": \"minecraft:uniform\",\n"),
			code("    \"min\": 4, \"max\": 6,\n"),
			code("}\n\n"),
			note("Perfect for ore-crushing and drops."),
		], line_width=CODE_W, scale=0.45),
		Page("Loot & Manual, For Free", [
			title("The payoff (6/6)\n\n"),
			body("Every item gets a "), hl("loot table"), body(", and a "),
			hl("_give_all"), body(" function hands out chests of everything you made - great for tests.\n\nBetter yet: every recipe is "), hl("rendered", "gold"),
			body(" into the in-game manual, automatically.\n\n"),
			note("Define once. Appreciate the rest.\n\n"),
			link("Docs: Definitions Setup", r"https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"),
		], scale=0.475),
	]),

	# 8 Generate Entire Material Sets
	Zone("Material Sets", (197, 102, -28), 0, [
		Page("One Config", [
			title("Describe it once (1/9)\n\n"),
			body("A new metal usually means dozens of items, models and recipes, all by hand.\n\nWith "), brand(), body(", you write "),
			hl("one"), body(" code block:\n\n"),
			code("ORES_CONFIGS = {\n"),
			code("    \"steel_ingot\": EquipmentsConfig(\n"),
			code("        equivalent_to=DefaultOre.IRON,\n"),
			code("    ),\n"),
			code("}"),
		], line_width=CODE_W, scale=0.5),
		Page("The Whole Family", [
			title("One line in, a set out (2/9)\n\n"),
			code("generate_everything_about_these_materials(ORES_CONFIGS)\n\n"),
			body("And out comes the whole family:\n\n"),
			code("steel_ingot, steel_nugget, raw_steel, steel_dust, steel_block, steel_ore, deepslate_steel_ore, ", color="#538b97"),
			code("steel_pickaxe, steel_axe, steel_sword, steel_shovel, steel_hoe, steel_spear, ", color="#70becf"),
			code("steel_helmet, steel_chestplate, steel_leggings, steel_boots, and more...\n\n", color="#538b97"),
			note("Around 20 items, from one config."),
		], line_width=225, scale=0.42),
		Page("Textures Lead", [
			title("Your art decides (3/9)\n\n"),
			brand(), body(" scans your textures folder and builds "), hl("only"), body(" what it finds there.\n\n"),
			body("Drop in a "), code("steel_sword.png", color="#8BE9FD"), body(" and a steel sword exists. No file, no item.\n\n"),
			note("Add the art, rebuild, it's there."),
		]),
		Page("Recipes Included", [
			title("Crafts, for free (4/9)\n\n"),
			body("Every generated item is already wired up:\n\n- Raw & dust "),
			hl("smelt"), body(" to the ingot\n- Shapeless: 9 ingots "),
			hl("<->"), body(" 1 block\n- Shapeless: 9 nuggets "), hl("<->"), body(" 1 ingot\n"),
			body("- Tools & armor get their crafting "), hl("shapes"), body("\n- Melt old gear back into "),
			hl("nuggets"), body("\n- The ore "), hl("drops"), body(" when no silk touch\n- ...\n\n"),
			note("Blasting + pulverizing (2x dust) too."),
		], scale=0.5, line_width=CODE_W),
		Page("Wears On Your Body", [
			title("Armor that renders (5/9)\n\n"),
			body("Add two layer textures beside the gear:\n\n"),
			code("steel_layer_1.png  # body & head\n"),
			code("steel_layer_2.png  # legs & feet\n\n"),
			brand(), body(" copies them into the assets/*/equipment folder and wires the "), hl("equippable"),
			body(" component - so your set actually shows "), hl("on the player", "gold"), body(", not just in the slot."),
		], line_width=CODE_W, scale=0.5),
		Page("Give It A Personality", [
			title("Not just a reskin (6/9)\n\n"),
			body("Make your config relative to a vanilla tier, and bend the numbers:\n\n"),
			code("equivalent_to = DefaultOre.IRON\n"),
			code("pickaxe_durability = 3 * iron\n"),
			code("attributes = {\n"),
			code("    \"attack_damage\": 1,      # +1 a hit\n"),
			code("    \"mining_efficiency\": 2,   # +20% speed\n"),
			code("}\n\n"),
			body("Steel: iron's stats, but the whole set is "), hl("3x tougher"), body(" and quicker to mine with."),
		], line_width=CODE_W, scale=0.45),
		Page("Pick Your Tier", [
			title("Any vanilla tier (7/9)\n\n"),
			body("Base the set on any tier: "),
			hl("wood"), body(", "), hl("stone"), body(", "), hl("gold"), body(", "), hl("copper"), body(", "), hl("iron"), body(", "), hl("diamond"), body(", "), hl("netherite"), body(".\n\n"),
			body("Modifiers auto-route: "), body("armor & toughness to "), hl("armor"), body(", "), hl("damage & mining to "), hl("tools"), body(".\n\n"),
			note("Stone -> chainmail armor,\nwood -> leather armor."),
		], line_width=195, scale=0.55),
		Page("Names & Overrides", [
			title("It reads your names (8/9)\n\n"),
			code("\"steel_ingot\"             -> steel\n"),
			code("\"minecraft:emerald\"     -> emerald\n"),
			code("\"adamantium_fragment\" -> adamantium\n"),
			code("\"awakened_stardust!\"  -> keep whole\n\n"),
			body("A trailing "), hl("!"), body(" keeps a multi-word base intact. Set "), hl("ignore_recipes=True"),
			body(" to keep the items but write the recipes yourself."),
		], line_width=CODE_W, scale=0.5),
		Page("Mix Anything", [
			title("Custom or vanilla (9/9)\n\n"),
			body("One dict can hold many materials at once, even vanilla ones:\n\n"),
			code("\"steel_ingot\": EquipmentsConfig(...),\n"),
			code("\"minecraft:emerald\": EquipmentsConfig(...),\n"),
			code("\"minecraft:stone\": None,\n\n"),
			body("Pass "), hl("None"), body(" for no stats: stone still finds your "),
			hl("stone_stick"), body(" and "), hl("stone_rod"), body(" textures on its own.\n\n"),
			link("Docs: Definitions Setup", r"https://stewbeet.paralya.fr/markdown?src=1_definitions_setup%2Fen.md"),
		], line_width=CODE_W, scale=0.5),
	]),

	# 9 The Interactive In-Game Manual
	Zone("In-Game Manual", (202, 102, -25), 180, [
		Page("Free Documentation", [
			title("A manual, generated (1/8)\n\n"),
			brand(), body(" builds a full "), hl("interactive"),
			body(" manual from your items and recipes.\n\n"),
			note("Every recipe, rendered and clickable.\n\n"),
			link("Please check the GIF!\nI highly recommend it!!!", r"https://github.com/Stoupy51/StewBeet/blob/main/docs/plugins/img/ingame_manual.gif"),
		], line_width=195),
		Page("Wiki Buttons", [
			title("Add your own notes (2/8)\n\n"),
			body("Give an item "), hl("wiki_buttons"),
			body(" and each one shows up as a hoverable button on its page:\n\n"),
			code("Item(\n"),
			code("    id=\"steel_ingot\",\n"),
			code("    wiki_buttons=[\n"),
			code("        WikiButton({\"text\": \"Any text component here.\"}),\n"),
			code("        WikiButton({\"text\": \"Another one!\", \"color\": \"aqua\"}),\n"),
			code("    ],\n"),
			code(")"),
		], line_width=250, scale=0.45),
		Page("Phase Hooks", [
			title("Hook the build (3/8)\n\n"),
			body("Default pages only exist "), hl("during", "gold"),
			body(" the build,\nso register a function at the right "), hl("Phase"), body(":\n\n"),
			code("manual = get_manual()\n\n"),
			code("@manual.on(Phase.PREPARED)\n"),
			code("def tweak(m: Manual):\n"),
			code("    page = m.get_page_for_item(\"steel_ingot\")\n\n"),
			note("DISCOVERED, PREPARED, ORDERED,\nRENDERED, RESOLVED, BEFORE_EMIT."),
		], line_width=250, scale=0.45),
		Page("Custom Pages", [
			title("Insert any page (4/8)\n\n"),
			body("Slot a "), hl("CustomPage"), body(" anywhere, even unrelated to items:\n\n"),
			code("manual.insert_page(CustomPage(\n"),
			code("    anchor=\"welcome\",\n"),
			code("    title=\"Welcome\",\n"),
			code("    body=[{\"text\": \"Hello!\"}],\n"),
			code("), after=\"intro\")\n\n"),
			body("Links are deferred ("), hl("PageRef"),
			body("): insert or reorder pages, navigation never breaks."),
		], line_width=CODE_W, scale=0.45),
		Page("Texture Pages", [
			title("Bring your own art (5/8)\n\n"),
			body("Back a page with a "), hl("texture"), body(", text baked into the image itself:\n\n"),
			code("manual.insert_page(TexturePage(\n"),
			code("    anchor=\"tutorial\",\n"),
			code("    title=\"Tutorial\",\n"),
			code("    background=\"assets/tutorial_bg.png\",\n"),
			code("    baked_texts=[BakedText(\n"),
			code("        text=\"Step 1: mine ore\",\n"),
			code("        xy=(20, 40),\n"),
			code("    )],\n"),
			code("), before=\"category:Materials\")"),
		], line_width=CODE_W, scale=0.45),
		Page("Button Layout", [
			title("Buttons, your way (6/8)\n\n"),
			body("Decide where wiki buttons go and how overflow is handled:\n\n"),
			code("page.button_layout = ButtonLayout(\n"),
			code("    columns=6,\n"),
			code("    max_buttons=42,\n"),
			code("    position=\"after_recipe\",\n"),
			code("    order=(lambda b: -b.priority),\n"),
			code(")\n\n"),
			note("Per page, or as the manual-wide default."),
		], line_width=CODE_W, scale=0.45),
		Page("Custom Recipe Types", [
			title("Render new crafts (7/8)\n\n"),
			body("One class + one call teaches the manual a whole new recipe type. The real "),
			hl("Pulverizer"), body(" support:\n\n"),
			code("class PulverizingRenderer(LinearRenderer):\n"),
			code("    types = (PulverizingRecipe.type,)\n"),
			code("    name = \"(SimplEnergy) Pulverizing\"\n\n"),
			code("    def static_glyph(self, craft):\n"),
			code("        return PULVERIZING_FONT\n\n"),
			code("register_craft_renderer(PulverizingRenderer())\n\n"),
			note("LinearRenderer draws the shared\n\"ingredient -> result\" row layout."),
		], line_width=250, scale=0.42),
		Page("Always Up To Date", [
			title("Never stale (8/8)\n\n"),
			body("Add an item, rebuild, and the manual updates "), hl("itself", "gold"), body(".\n\n"),
			note("Dialog UI, can be opened from the vanilla quick actions menu.\n\n"),
			link("Docs: In-Game Manual", r"https://stewbeet.paralya.fr/markdown?src=7_ingame_manual%2Fen.md"),
		]),
	]),

	# 10 Quality of Life + Ecosystem
	Zone("QoL + Ecosystem", (203, 102, -28), 0, [
		Page("Auto Everything", [
			title("It writes the chores (1/6)\n\n"),
			body("- "), hl("en_us.json"), body(" lang file\n "),
			link("[auto.lang_file]", r"https://stewbeet.paralya.fr/markdown?src=plugins/auto.lang_file.md"),
			body("\n\n- Function "), hl("headers\n "),
			link("[auto.headers]", r"https://stewbeet.paralya.fr/markdown?src=plugins/auto.headers.md"),
			body("\n\n- Scoreboard "), hl("constants"), body(" detection\n "),
			link("[auto.scoreboard_constants]", r"https://stewbeet.paralya.fr/markdown?src=plugins/auto.scoreboard_constants.md"),
			note("\n\nDetected from your code, automatically."),
		], line_width=CODE_W, scale=0.5),
		Page("Library Magic", [
			title("Libraries, auto-wired (2/6)\n\n"),
			body("Use a Bookshelf or Smithed feature and the dependency is added for you:\n\n"),
			hl("Bookshelf, Smithed Crafter & Blocks, ItemIO, Common Signals, and more.\n\n"),
			link("Docs: Libraries Support", r"https://stewbeet.paralya.fr/markdown?src=5_dependencies%2Fen.md"),
		]),
		Page("Ship It", [
			title("From build to release (3/6)\n\n"),
			body("- Merge with "), hl("Smithed Weld\n "),
			link("[merge_smithed_weld]", r"https://stewbeet.paralya.fr/markdown?src=plugins/merge_smithed_weld.md"),
			body("\n\n- "), hl("SHA1"), body(" hashes for servers\n "),
			link("[compute_sha1]", r"https://stewbeet.paralya.fr/markdown?src=plugins/compute_sha1.md"),
			body("\n\n- Auto-copy (works with "), hl("sftp"), body(" too)\n "),
			link("[copy_to_destination]", r"https://stewbeet.paralya.fr/markdown?src=plugins/copy_to_destination.md"),
			body("\n\n- Continuous Delivery\n"), hl("(Modrinth, Smithed, PMC, GitHub)\n "),
			link("[Full Detailed Guide]", r"https://stewbeet.paralya.fr/markdown?src=6_continuous_delivery%2Fen.md"),
			note("\n\nReady to publish in one command."),
		], line_width=CODE_W, scale=0.425),
		Page("Compatibilities", [
			title("Plays well with others (4/6)\n\n"),
			body("Automatic special support for:"),
			body("\n\n- SimpleDrawer compacted drawers\n "),
			link("[compatibilities.simpledrawer]", r"https://stewbeet.paralya.fr/markdown?src=plugins/compatibilities.simpledrawer.md"),
			body("\n\n- NeoEnchant veinminer\n "),
			link("[compatibilities.neo_enchant]", r"https://stewbeet.paralya.fr/markdown?src=plugins/compatibilities.neo_enchant.md"),
			body("\n\n- SimplEnergy pulverizer\n "),
			link("[PulverizingRecipe]", r"https://stoupy51.github.io/StewBeet/latest/modules/stewbeet.core.cls.recipe.html#stewbeet.core.cls.recipe.PulverizingRecipe"),
		], line_width=CODE_W, scale=0.5),
		Page("Get StewBeet", [
			title("Try it today (5/6)\n\n"),
			cmd("pip install stewbeet\n\n"),
			link("Join the Discord community!", r"https://discord.gg/anxzu6rA9F"), body("\n"),
			link("Docs: stewbeet.paralya.fr", r"https://stewbeet.paralya.fr"),
		], line_width=CODE_W),
		Page("Thank You", [
			title("Thank you! (6/6)\n\n"),
			body("Build more. Write less.\n\nPowered by "), *brand(), body(".\n\n"),
			note("Curious about how this booth was made? Check the source code at\n"), link("github.com/Stoupy51/SmithedSummit2026", r"https://github.com/Stoupy51/SmithedSummit2026"),
		], line_width=CODE_W, scale=0.5),
	]),


	## Underground
	# My projects
	Zone("My Projects", (202, 54, -25), -135, [
		Page("My Projects", [
			title("My Projects\n\n"),
			body("Welcome to the Switch Space!\nYou'll find a variety of my projects here, all built on "), brand(), body(".\n\n"),
			body("This black hole is a part of the lobby of my project "), hl("Switch Minigames"),
			body(", check the zone on the right for more details.\n\n"),
			body("The 3 other zones are split in 3 categories:\n"),
			body("- My "), hl("released"), body(" datapacks\n"),
			body("- My "), hl("WIP"), body(" datapacks\n"),
			body("- Myself, the developer"),
		], line_width=CODE_W, scale=0.45),
	]),
	Zone("Switch Minigames", (198, 54, -28), 0, [
		Page("Switch Minigames", [
			title("Switch Minigames (1/3)\n\n"),
			body("A "), hl("democratic", "gold"),
			body(" minigame server, always on the latest Minecraft version. Still in beta, soon to be released as a public server.\n\n"),
			link("Be notified of updates", r"https://discord.gg/anxzu6rA9F"), body("\n"),
			link("Terrifying source code", r"https://github.com/Paralya/Switch"),
		]),
		Page("The Vote", [
			title("Democracy! (2/3)\n\n"),
			body("At the end of each round, a "), hl("vote"), body(" decides the next minigame (7 options):\n\n"),
			body("- Option 1 replays the last game,\n  great for a loop of "), hl("fuuuun", "gold"), body("\n"),
			body("- Options 2-7 are random picks based on the player count\n"),
			body("- The 7th hides its pick under the name "), hl("\"Random\""), body("\n\n"),
			note("15 seconds to vote,\nchange it anytime until the end."),
		], line_width=CODE_W, scale=0.45, sticker="switch_minigames"),
		Page("The Minigames", [
			title("50+ minigames (3/3)\n\n"),
			body("The initial goal was 48... we now aim for an "), hl("infinite", "gold"), body(" number!\n\n"),
			body("Spend the server's "), hl("Sapphire"), body(" currency on cosmetic advantages in certain games.\n\n"),
			link("2 years of memories (video)", r"https://www.youtube.com/watch?v=cB27sEOxboA"),
		]),
	]),
	Zone("Released Datapacks", (205, 54, -21), 90, [
		Page("LifeSteal FR", [
			title("LifeSteal FR (1/6)\n\n"),
			body("The Lifesteal SMP experience:\nkill a player, "), hl("steal a heart", "red"), body(".\n\n"),
			body("Craft hearts, revive the fallen with "), hl("revive beacons"),
			body(", and tune every rule from an in-game "), hl("config"), body(" menu.\n\n"),
			link("[PMC]", r"https://www.planetminecraft.com/data-pack/life-steal-fr/"), body(" "),
			link("[Modrinth]", r"https://modrinth.com/datapack/lifestealfr"), body(" "),
			link("[GitHub]", r"https://github.com/Stoupy51/LifeSteal"),
		]),
		Page("SimplEnergy", [
			title("SimplEnergy (2/6)\n\n"),
			body("Simple "), hl("energy", "gold"), body(" for survival: solar panels, 3 battery tiers, energy and item cables, electric furnaces, pulverizers...\n\n"),
			body("Also a clean "), hl("template"), body(" for building your own energy datapack with "), brand(), body(".\n\n"),
			link("[PMC]", r"https://www.planetminecraft.com/data-pack/simplenergy/"), body(" "),
			link("[Modrinth]", r"https://modrinth.com/datapack/simplenergy"), body(" "),
			link("[GitHub]", r"https://github.com/Stoupy51/SimplEnergy"),
		], line_width=CODE_W, scale=0.5, sticker="simplenergy"),
		Page("Stardust Fragment", [
			title("Stardust Fragment (3/6)\n\n"),
			body("A whole tech-adventure progression:\n\n"),
			body("- "), hl("190+"), body(" items across 6 tiers\n"),
			body("- "), hl("35+"), body(" energy devices\n"),
			body("- "), hl("5"), body(" custom dimensions\n"),
			body("- mini-bosses & end-game bosses\n"),
			body("- "), hl("100+"), body(" advancements & manual pages\n\n"),
			link("[PMC]", r"https://www.planetminecraft.com/data-pack/stardust-fragment/"), body(" "),
			link("[Modrinth]", r"https://modrinth.com/datapack/stardust-fragment"), body(" "),
			link("[GitHub]", r"https://github.com/Stoupy51/StardustFragment"),
		], line_width=CODE_W, scale=0.45),
		Page("Random Mob Sizes", [
			title("Random Mob Sizes (4/6)\n\n"),
			body("Every mob spawns at a random "), hl("scale"), body(" for varied encounters.\n\n"),
			body("Optionally ties "), hl("health"), body(", "), hl("speed"), body(" and "), hl("damage"),
			body(" to the size, with per-mob overrides and an in-game config.\n\n"),
			link("[PMC]", r"https://www.planetminecraft.com/data-pack/random-mob-sizes-6264344/"), body(" "),
			link("[Modrinth]", r"https://modrinth.com/datapack/random-mob-sizes-dp"), body(" "),
			link("[GitHub]", r"https://github.com/Stoupy51/RandomMobSizes/releases/latest"),
		], scale=0.5),
		Page("My Libraries", [
			title("My libraries (5/6)\n\n"),
			body("Shared building blocks,\nfree to use in your own packs:\n\n"),
			link("[Realistic Explosion]", r"https://github.com/Stoupy51/RealisticExplosion"), body(" optimized realistic blasts\n"),
			link("[Furnace NBT Recipes]", r"https://github.com/Stoupy51/FurnaceNbtRecipes"), body(" custom furnace recipes\n"),
			link("[Smart Ore Generation]", r"https://github.com/Stoupy51/SmartOreGeneration"), body(" custom ore veins\n"),
			link("[Common Signals]", r"https://github.com/Stoupy51/CommonSignals"), body(" shared selectors & hooks"),
		], line_width=275, scale=0.55),
		Page("And More", [
			title("...and more! (6/6)\n\n"),
			body("Check my profiles for the full collection:\n\n"),
			link("planetminecraft.com/member/stoupy", r"https://www.planetminecraft.com/member/stoupy/"), body("\n"),
			link("modrinth.com/user/Stoupy51", r"https://modrinth.com/user/Stoupy51"), body("\n\n"),
			note("100% of them powered by StewBeet."),
		], line_width=CODE_W),
	]),
	Zone("WIP Datapacks", (198, 54, -14), 180, [
		Page("MC Guns System", [
			title("MC Guns System (1/6)\n\n"),
			body("A full "), hl("FPS framework", "gold"), body(" for Minecraft: a complete rewrite of MGS 4.2, built with "), brand(), body(".\n\n"),
			body("Weapons are "), hl("data-driven"), body(": all the stats live on the items, not in hardcoded logic.\n\n"),
			link("github.com/Stoupy51/MC_Guns_System", r"https://github.com/Stoupy51/MC_Guns_System"),
		], line_width=CODE_W),
		Page("The Weapons", [
			title("The weapon framework (2/6)\n\n"),
			body("- "), hl("Hit detection"), body(" raycasts with spread & headshot detection\n"),
			body("- Slow projectiles ("), hl("RPG"), body(") and throwable "), hl("grenades"), body("\n"),
			body("- Ammo, reload & reserve tracking\n"),
			body("- Fire modes: "), hl("semi"), body(", "), hl("auto"), body(", "), hl("burst"), body("\n"),
			body("- Recoil & casing ejection\n"),
			body("- Lore generated from the stats"),
		], line_width=CODE_W),
		Page("Game Modes", [
			title("Three game families (3/6)\n\n"),
			body("- "), hl("Multiplayer"), body(": FFA, Team Deathmatch, Domination, Hardpoint, Search & Destroy\n\n"),
			body("- "), hl("Missions"), body(": co-op PvE with waypoints navigation to targets\n\n"),
			body("- "), hl("Zombies"), body(": round-based survival with perks, mystery box, traps..."),
		], line_width=CODE_W),
		Page("Map Editor", [
			title("In-game map editor (4/6)\n\n"),
			body("One generic tool for "), hl("storage-based"), body(" maps for all three families:\n\n"),
			body("spawns, boundaries, objectives, doors, wallbuys, traps, perk machines...\n\n"),
			body("Relative coordinates make maps "), hl("portable", "gold"), body(" and shareable across projects."),
		], line_width=CODE_W),
		Page("Loadouts", [
			title("Loadouts & classes (5/6)\n\n"),
			body("Build your class with "), hl("pick-10"), body(" style constraints and perk selection.\n\n"),
			body("Browse a "), hl("marketplace"), body(" of player-made loadouts: filter, favorite, share public or keep private."),
		], line_width=CODE_W),
		Page("ImagineYourCraft", [
			title("ImagineYourCraft (6/6)\n"),
			note("Totally unrelated to MGS.\n\n"),
			body("Recreating an old modded server's mod as a pure "), hl("datapack", "gold"), body(".\n\n"),
			link("github.com/Stoupy51/ImagineYourCraftDatapack", r"https://github.com/Stoupy51/ImagineYourCraftDatapack"),
		]),
	]),
	Zone("Myself", (191, 54, -21), -90, [
		Page("Who Am I?", [
			note("Better to introduce myself now than never.\n\n"),
			title("Hi, I'm Stoupy! (1/3)\n\n"),
			body("Playing Minecraft since the "), hl("1.0", "gold"),
			body(" release month (November 2011), doing "), hl("command blocks", "gold"),
			body(" since they were added, and "), hl("datapacks", "gold"), body(" since 1.15: "),
			hl("7 years"), body(" ago.\n\n"),
			link("github.com/Stoupy51", r"https://github.com/Stoupy51"),
		], line_width=CODE_W),
		Page("Jobs", [
			title("Jobs (2/3)\n\n"),
			body("- "), hl("Data Scientist"), body(" in Health,\nas a full-time job IRL\n"),
			body("- "), hl("Sys Admin"), body(" of Survisland,\na Survivor (TV-show) like community\n"),
			body("- "), hl("Administrator"), body(" of Paralya,\na french-speaking Minecraft commuinity\n"),
			body("- 23 years old, "), hl("French ", "gold"),
			{"text": "(unfortunately)", "color": "#7F8C99", "italic": True, "strikethrough": True}, body("\n"),
			body("- Speaking English, French and 日本語")
		], line_width=CODE_W),
		Page("Always Building", [
			title("Always building (3/3)\n\n"),
			body("A very active developer: over "), hl("3,000 commits", "gold"), body(" per year on GitHub.\n\n"),
			link("github.com/Stoupy51", r"https://github.com/Stoupy51"), body("\n\n"),
			note("Thanks for stopping by!"),
		]),
	]),
]

