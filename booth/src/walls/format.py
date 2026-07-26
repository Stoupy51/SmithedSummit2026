""" Text-component styling helpers for the presentation-wall content.

Minecraft's font has no emoji glyphs, so pages lean on color + bold instead.
Each helper returns a single text-component dict, except the wordmarks and
syntax-highlighted code, which return a list of components.
"""

# Imports
import re

from stewbeet import create_gradient_text
from stouputils.typing import JsonDict


def brand() -> list[JsonDict]:
	""" The 'StewBeet' wordmark as a green->red gradient. """
	return create_gradient_text("StewBeet", "#FF9100", "#FF0000")

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

def note(text: str) -> JsonDict:
	""" A gray italic aside. """
	return {"text": text, "color": "#7F8C99", "italic": True}


# --- Code syntax highlighting -------------------------------------------------
# A small, forgiving tokenizer: good enough for the short Python-ish snippets on
# the walls (also degrades gracefully on YAML / shell lines). Dracula-ish palette
# on Minecraft's dark background; the old flat code color (#8BE9FD) becomes the
# "type" color so existing snippets keep their familiar look.
C_COMMENT: str = "#6272A4"  # grey-blue
C_STRING:  str = "#F1FA8C"  # yellow
C_NUMBER:  str = "#BD93F9"  # purple
C_KEYWORD: str = "#FF79C6"  # pink (keywords + assignment/arrow operators)
C_TYPE:    str = "#8BE9FD"  # cyan  (Capitalized names: classes / enums)
C_CALL:    str = "#50FA7B"  # green (lowercase name directly before '(')
C_FG:      str = "#F8F8F2"  # near-white (plain identifiers, punctuation)

KEYWORDS: frozenset[str] = frozenset({
	"def", "return", "import", "from", "for", "in", "if", "else", "elif", "None",
	"True", "False", "class", "with", "as", "pass", "and", "or", "not", "is",
	"lambda", "while", "try", "except", "finally", "raise", "yield", "global",
	"nonlocal", "assert", "del", "async", "await", "break", "continue",
})
PINK_OPS: frozenset[str] = frozenset({
	"->", "=", "==", "+", "-", "*", "/", "%", "<", ">", "<=", ">=", "!=", "+=", "-=",
})

TOKEN_RE: re.Pattern[str] = re.compile(
	r'(?P<comment>\#[^\n]*)'
	r'|(?P<string>"[^"\n]*"|\'[^\'\n]*\')'
	r'|(?P<number>\b\d+\.?\d*\b)'
	r'|(?P<name>[A-Za-z_][A-Za-z0-9_]*)'
	r'|(?P<ws>\s+)'
	r'|(?P<op>->|[-+*/%=<>!]=?|[.,:;()\[\]{}])'
	r'|(?P<other>.)'
)


def token_color(m: re.Match[str]) -> str | None:
	""" Map a matched token to its color, or None to inherit (neutral). """
	kind: str | None = m.lastgroup
	text: str = m.group()
	if kind == "comment":
		return C_COMMENT
	if kind == "string":
		return C_STRING
	if kind == "number":
		return C_NUMBER
	if kind == "op":
		return C_KEYWORD if text in PINK_OPS else C_FG
	if kind == "name":
		if text in KEYWORDS:
			return C_KEYWORD
		# A name immediately followed by '(' is a call; Capitalized -> a type.
		rest: str = m.string[m.end():].lstrip(" \t")
		if rest[:1] == "(":
			return C_TYPE if text[:1].isupper() else C_CALL
		return C_TYPE if text[:1].isupper() else C_FG
	return None  # whitespace / stray chars -> no color


def highlight_code(text: str) -> list[str | JsonDict]:
	""" Tokenize a code fragment into per-token colored components.

	Returns a component list (leading "" so siblings don't inherit formatting).
	Consecutive same-color tokens are merged to keep the NBT small.
	"""
	out: list[JsonDict] = []
	for m in TOKEN_RE.finditer(text):
		color: str | None = token_color(m)
		if out and out[-1].get("color") == color:
			out[-1]["text"] += m.group()
		else:
			comp: JsonDict = {"text": m.group()}
			if color:
				comp["color"] = color
			out.append(comp)
	return ["", *out]


def code(text: str, color: str | None = None) -> JsonDict | list[str | JsonDict]:
	""" A code fragment.

	Without `color`, it is syntax-highlighted (Python-ish). Pass a `color` to
	render the whole fragment in that single flat color instead (handy for
	non-code snippets like plain item-name lists).
	"""
	if color is None:
		return highlight_code(text)
	return {"text": text, "color": color}

def cmd(text: str) -> JsonDict:
	""" A shell / CLI command line. Flat cyan so it reads as a command and does
	not blend with body text (the Python highlighter would leave it plain). """
	return {"text": text, "color": "#8BE9FD"}

