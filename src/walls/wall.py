""" Per-wall derived data: slugs, function paths, scoreboard names, UUIDs.

zone_slug() / unique_slugs() turn zone titles into filesystem-friendly folder
names; the Wall class bundles every identifier the writer modules (summons,
pages, animation, navigation) need for one zone, so they never re-derive them.
"""

# Imports
import re

from .content import Page, Zone
from .links import collect_links
from .settings import PAGE_SCALE


def zone_slug(name: str) -> str:
	""" Filesystem-friendly folder name for a zone, from its title
	(e.g. 'Recipes & Loot' -> 'recipes_loot'). """
	return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def unique_slugs(zones: list[Zone]) -> list[str]:
	""" zone_slug for each zone, disambiguating any collision with a numeric suffix. """
	slugs: list[str] = []
	for zi, zone in enumerate(zones):
		slug: str = zone_slug(zone.name)
		if slug in slugs:
			slug = f"{slug}_{zi}"
		slugs.append(slug)
	return slugs


class Wall:
	""" Everything derived from one Zone that the wall writers need.

	Holds the zone itself plus the naming glue: the function-path prefix
	(`base`), the scoreboard fake-player holding the page index (`holder`), the
	two scoreboard objectives, the summon anchor, and the fixed UUIDs of the
	wall's dynamic entities. Build one per zone and pass it around.
	"""

	def __init__(self, ns: str, index: int, zone: Zone, slug: str) -> None:
		""" Derive every identifier for the wall at `index` in TEXTS.

		Args:
			ns    (str):  project namespace (e.g. 'stewbeet_summit')
			index (int):  zone position in TEXTS (also seeds the fixed UUIDs)
			zone  (Zone): the wall's content (title, coords, rotation, pages)
			slug  (str):  this zone's entry from unique_slugs(TEXTS)
		"""
		self.ns: str = ns
		self.index: int = index
		self.zone: Zone = zone
		self.slug: str = slug

		self.base: str = f"{ns}:walls/{slug}"       # function-path prefix for this wall
		self.holder: str = f"#{slug}"               # scoreboard fake-player holding the page index
		self.page_objective: str = f"{ns}.page"     # objective: current page index
		self.fade_objective: str = f"{ns}.data"       # objective: fade phase countdown

		# Summon anchor: centered on the anchor block, one block down, facing the
		# zone's rotation. All local-frame (^) offsets are relative to this.
		x, y, z = zone.coords
		self.yaw: int = zone.rotation
		self.anchor: str = f"positioned {x + 0.5} {y - 1.0} {z + 0.5} rotated {self.yaw} 0"
		self.rotation: list[int] = [self.yaw, 0]    # entity Rotation NBT (yaw, pitch)

		self.page_count: int = len(zone.pages)

		# Fixed UUIDs for this wall's dynamic entities (page, both arrows and, on
		# walls with links, the "Open link" prompt + its interaction), so the page
		# functions target them directly (no per-tick @e tag scan).
		self.page_uuid: str = f"20180612-2026-2002-2098-2020{index:08d}"
		self.left_arrow_uuid: str = f"20180612-2026-2002-2098-2021{index:08d}"
		self.right_arrow_uuid: str = f"20180612-2026-2002-2098-2022{index:08d}"
		self.link_prompt_uuid: str = f"20180612-2026-2002-2098-2023{index:08d}"
		self.link_interaction_uuid: str = f"20180612-2026-2002-2098-2024{index:08d}"

		# Links present on each page (empty list = none). A wall gets its centered
		# "Open link" prompt + interaction only when at least one page has a link.
		self.page_links: list[list[tuple[str, str]]] = [collect_links(p.text) for p in zone.pages]
		self.has_links: bool = any(self.page_links)

	def function(self, name: str) -> str:
		""" Full function path for `name` under this wall's folder
		(e.g. wall.function('show') -> '<ns>:walls/<slug>/show'). """
		return f"{self.base}/{name}"

	def page_scale(self, page: Page) -> float:
		""" The text_display scale for a page: its own override, or the global PAGE_SCALE. """
		return page.scale if page.scale is not None else PAGE_SCALE
