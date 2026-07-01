""" Small helpers for display-entity NBT and SNBT command fragments.

Shared by the presentation walls (src/walls) and the entrance decorations
(src/intro). These turn Python dicts into the string forms Minecraft commands
expect: `nbt()` for a full component (modern SNBT accepts this JSON form),
`dump()` for splicing inside an existing `{...}`, and `with_uuid()` for pinning a
fixed entity UUID so functions can target the entity directly instead of scanning tags.
"""

# Imports
import json
from typing import Any

from stewbeet import Mem
from stouputils.typing import JsonDict


def scale_only(sx: float, sy: float, sz: float) -> JsonDict:
	""" A display `transformation` with only scale set (identity rotation, no translation). """
	return {
		"left_rotation": [0.0, 0.0, 0.0, 1.0],
		"right_rotation": [0.0, 0.0, 0.0, 1.0],
		"scale": [sx, sy, sz],
		"translation": [0.0, 0.0, 0.0],
	}

def item_nbt(item: str, **kwargs: Any) -> JsonDict:
	""" NBT for a static item_display showing the project's `item` model. """
	ns: str = Mem.ctx.project_id
	return {
		"item": {
			"id": "stone",
			"components": {"minecraft:item_model": f"{ns}:{item}"},
			"count": 1,
		},
		"Tags": [f"{ns}.{item}", f"{ns}.entity", "summit.static"],
		"brightness": {"block": 15, "sky": 15},
		**kwargs,
	}

def dump(obj: Any) -> str:
	""" JSON for `obj` without its surrounding braces, to splice inside an existing `{...}`. """
	return json.dumps(obj)[1:-1]

def nbt(obj: Any) -> str:
	""" Full SNBT-compatible serialization (modern SNBT accepts this JSON form). """
	return json.dumps(obj, ensure_ascii=False)

def root(components: Any) -> list[Any]:
	""" Wrap components with an empty root so siblings don't inherit the first
	element's formatting (a bold title would otherwise bold the whole page). """
	return ["", *components]

def with_uuid(uuid: str, obj: JsonDict) -> str:
	""" SNBT for `obj` with a fixed `UUID:uuid("...")` spliced in, so the entity
	can be selected directly by UUID instead of by tag. """
	return '{UUID:uuid("' + uuid + '"),' + nbt(obj)[1:]
