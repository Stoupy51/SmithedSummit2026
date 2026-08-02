""" Smithed Summit 2026 stage screen geometry.

Reef derives the in-game slideshow size straight from the PDF page size: one PDF point is one
model pixel, which is 1/16 of a block. A 336 x 192 pt page therefore renders as a 21 x 12 block screen.
Element positions use the top-left corner of the slide as the origin, with +X going right and -Y going down.
"""
# Imports
from dataclasses import dataclass

# Constants
POINTS_PER_BLOCK: int = 16
""" A Reef element is built from a 1x1 model-pixel quad, and a model pixel is 1/16 of a block. """


# Classes
@dataclass(frozen=True)
class Stage:
	""" One Smithed Summit stage screen, sized from the official presentation template. """

	key: str
	""" Short identifier used in file names and log messages. """
	display_name: str
	""" Human readable stage name, as the Summit team calls it. """
	page_width: int
	""" Slide width in PDF points, which must match the exported presentation exactly. """
	page_height: int
	""" Slide height in PDF points. """
	screen_tag: str
	""" Entity tag the Summit datapack puts on this stage's Reef screen. """

	@property
	def blocks_wide(self) -> float:
		""" Screen width in blocks.

		Examples:
			>>> WELDED_WOODLANDS.blocks_wide
			21.0
		"""
		return self.page_width / POINTS_PER_BLOCK

	@property
	def blocks_tall(self) -> float:
		""" Screen height in blocks.

		Examples:
			>>> WELDED_WOODLANDS.blocks_tall
			12.0
		"""
		return self.page_height / POINTS_PER_BLOCK

	@property
	def center(self) -> tuple[float, float, float]:
		""" Element position that lands in the middle of the slide.

		Examples:
			>>> WELDED_WOODLANDS.center
			(10.5, -6.0, 0)
		"""
		return (self.blocks_wide / 2, -self.blocks_tall / 2, 0)

	def texture_size(self, dpi: int) -> tuple[int, int]:
		""" Size in pixels of the texture Reef bakes for one slide at the given rasterization dpi.

		Args:
			dpi (int): Rasterization dpi, should be a multiple of 72 to stay on integer pixels.
		Returns:
			tuple[int, int]: Texture width and height in pixels.

		Examples:
			>>> WELDED_WOODLANDS.texture_size(144)
			(672, 384)
		"""
		return (round(self.page_width * dpi / 72), round(self.page_height * dpi / 72))


# Constants
STAGES: list[Stage] = [
	Stage(key="patched_plateaus_main", display_name="Patched Plateaus (Main)", page_width=546, page_height=269, screen_tag="summit.stages.patched_plateaus.screen.main"),
	Stage(key="patched_plateaus_side", display_name="Patched Plateaus (Side)", page_width=273, page_height=167, screen_tag="summit.stages.patched_plateaus.screen.side"),
	Stage(key="textured_tropics",      display_name="Textured Tropics",        page_width=400, page_height=224, screen_tag="summit.stages.textured_tropics.screen"),
	Stage(key="welded_woodlands",      display_name="Welded Woodlands",        page_width=336, page_height=192, screen_tag="summit.stages.welded_woodlands.screen"),
]
""" Every Summit stage, measured from the official templates in Trioplane/reef -> other_packs/reef_summit. """

WELDED_WOODLANDS: Stage = STAGES[3]
""" Stage this panel is presented on. Change TARGET_STAGE below if the Summit team moves us elsewhere. """

TARGET_STAGE: Stage = WELDED_WOODLANDS
""" Stage the presentation PDF must be exported for. Everything else is derived from it. """
