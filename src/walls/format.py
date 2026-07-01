""" Text-component styling helpers for the presentation-wall content.

Minecraft's font has no emoji glyphs, so pages lean on color + bold instead.
Each helper returns a single text-component dict, except the wordmarks which
return a gradient (a list of components).
"""

# Imports
from stewbeet import create_gradient_text
from stouputils.typing import JsonDict


def brand() -> list[JsonDict]:
	""" The 'StewBeet' wordmark as a green->red gradient. """
	return create_gradient_text("StewBeet", "#00FF00", "#FF0000")

def beet() -> list[JsonDict]:
	""" The 'Beet' wordmark as a green->red gradient. """
	return create_gradient_text("Beet", "#00C400", "#FF0000")

def title(text: str) -> JsonDict:
	""" A bold gold page title. """
	return {"text": text, "bold": True, "color": "gold"}

def body(text: str, color: str = "white") -> JsonDict:
	""" A plain run of body text. """
	return {"text": text, "color": color}

def hl(text: str, color: str = "aqua") -> JsonDict:
	""" An inline highlighted (bold) word. """
	return {"text": text, "bold": True, "color": color}

def code(text: str) -> JsonDict:
	""" A monospace-blue code fragment. """
	return {"text": text, "color": "#8BE9FD"}

def note(text: str) -> JsonDict:
	""" A gray italic aside. """
	return {"text": text, "color": "#7F8C99", "italic": True}

