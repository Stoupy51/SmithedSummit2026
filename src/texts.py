
# Imports
from dataclasses import dataclass

from stewbeet import TextComponent, create_gradient_text

# Constants
"""
- Text on walls (one topic at a time) with arrows to navigate "pages" (topics might change):
  - Topic 1 : What is StewBeet?
  - Topic 2 : Why? For who?
  - Topic 3 : Best Features (w/ example use cases)
    - Automatic Generation of loot tables, give command, conventions (lantern load, ...), recipes, etc.
    - Automatic Manual Generation
    - Easy custom blocks (with fortune, silk touch, and ore generation support)
    - Automatic Dependencies
  - Topic 4 : More niche but QOL features (w/ example use cases)
    - Auto lang file & auto headers
    - Continuous Delivery
    - Sounds.json & jukebox disc auto generated
    - ...

I have 10 walls.
"""

# https://minecraft.wiki/w/Display#Entity_data
@dataclass
class Page:
    name: str
    text: TextComponent
    line_width: int = 100

@dataclass
class Zone:
    name: str
    coords: tuple[int, int, int]
    rotation: int
    pages: list[Page]

TEXTS: list[Zone] = [
    Zone(
        "What is StewBeet?", (211, 102, -19), 90, [
            Page("Introduction", [
                {"text": "StewBeet is a "},
                create_gradient_text("Beet", "#00FF00", "#FF0000"),
                {"text": " framework providing powerful automation for Minecraft datapacks. Adaptable to "},
                create_gradient_text("any workflow", "#FFC400", "#FF9100"),
                {"text": "—use only the features you need, or leverage the full suite for complete project generation."},
            ]),
            Page("The Problem", [
                {"text": "Creating a datapack requires manually writing hundreds of JSON files, models, textures, functions..."},
            ]),
            Page("The Solution", [
                {"text": "StewBeet automates EVERYTHING: resource pack generation, models, custom blocks, recipes, and much more!"},
            ]),
            Page("The Result", [
                {"text": "Focus on YOUR creation, not files. Define your items and let StewBeet generate the rest."},
            ]),
        ]
    ),
    Zone()
]

