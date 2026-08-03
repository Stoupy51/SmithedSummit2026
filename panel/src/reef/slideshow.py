""" Turns the presentation PDF into a Reef slideshow.

The PDF is handed to Reef untouched, so the baked textures keep the full resolution of the export.
Reef sizes an element from the PDF page size, which would make a 1920x1080 pt deck a 120x67 block
wall, so each slide is shrunk back to the stage with the display entity's own scale instead.

That means the pages are built here rather than through a `reef:pdf` special definition, which
also gives per-slide commands for free.
"""
# Imports
import json
from dataclasses import dataclass, field
from pathlib import Path

from pypdf import PdfReader
from stewbeet import Mem, write_load_file
from stouputils.print import info, warning

from reef.assets.pdf import ReefPdfAsset
from reef.data.page import ReefPageData
from reef.data.slideshow import ReefSlideshowData

from .stages import POINTS_PER_BLOCK, TARGET_STAGE, Stage

# Constants
SOURCE_PDF: str = "How to Boost your Productivity.pdf"
""" Presentation export sitting next to beet.yml. Re-export over this file to update the slides, at any page size. """

SLIDESHOW_NAME: str = "panel"
""" Path of the generated slideshow, loaded in game as `<namespace>:panel`. """

MAX_MARGIN_RATIO: float = 0.02
""" Border left by fitting the slides, past which the export aspect ratio is worth complaining about. """


# Classes
@dataclass(frozen=True)
class PageOverride:
	""" Commands Reef runs around one slide. """

	on_load: list[str] = field(default_factory=list[str])
	""" Runs once when the slideshow is loaded onto a screen. """
	on_enter: list[str] = field(default_factory=list[str])
	""" Runs every time the slide is shown. """
	on_unload: list[str] = field(default_factory=list[str])
	""" Runs when the slideshow is cleared. """

	def to_commands(self) -> dict[str, list[str]]:
		""" Convert to the `commands` object of a Reef page.

		Returns:
			dict[str, list[str]]: Only the command lists that are not empty.

		Examples:
			>>> PageOverride(on_enter=["say hi"]).to_commands()
			{'on_enter': ['say hi']}
		"""
		named_commands: tuple[tuple[str, list[str]], ...] = (
			("on_load",   self.on_load),
			("on_enter",  self.on_enter),
			("on_unload", self.on_unload),
		)
		return {name: commands for name, commands in named_commands if commands}


@dataclass(frozen=True)
class Placement:
	""" How one slide has to be scaled and offset to land on the stage screen. """

	scale: float
	""" Factor shrinking the slide down to the screen, applied to the display entity. """
	offset_x: float
	""" Blocks between the left edge of the screen and the slide. """
	offset_y: float
	""" Blocks between the top edge of the screen and the slide. """

	@staticmethod
	def fit(page_size: tuple[int, int], stage: Stage) -> Placement:
		""" Fit a page onto a stage screen, keeping its aspect ratio and centring what is left over.

		Args:
			page_size (tuple[int, int]): Page width and height of the exported PDF, in points.
			stage     (Stage):           Stage the slides have to fit.
		Returns:
			Placement: Scale and offsets to put on every slide element.

		Examples:
			>>> from .stages import WELDED_WOODLANDS
			>>> Placement.fit((336, 192), WELDED_WOODLANDS)
			Placement(scale=1.0, offset_x=0.0, offset_y=0.0)
		"""
		scale: float = min(stage.page_width / page_size[0], stage.page_height / page_size[1])
		return Placement(
			scale=scale,
			offset_x=(stage.page_width - page_size[0] * scale) / 2 / POINTS_PER_BLOCK,
			offset_y=(stage.page_height - page_size[1] * scale) / 2 / POINTS_PER_BLOCK,
		)


# Constants
PAGE_OVERRIDES: dict[int, PageOverride] = {
	# Slide indexes are 0-based. Example, handing out the tomatoes when the AI slide shows up:
	# 12: PageOverride(on_enter=["function stoupy:tomato/give"], on_unload=["function stoupy:tomato/clear"]),
}
""" Per-slide commands, merged into the generated pages. """


class ReefSlideshow:
	""" Build-time generation of the panel slideshow out of the presentation PDF. """

	@staticmethod
	def read_pdf(pdf_path: Path) -> tuple[int, tuple[int, int]]:
		""" Read the slide count and the page size straight out of the presentation.

		The size comes from the first page only, since Reef gives every slide the size of the PDF.

		Args:
			pdf_path (Path): Presentation to inspect.
		Returns:
			tuple[int, tuple[int, int]]: Slide count, then page width and height in points.
		"""
		reader: PdfReader = PdfReader(pdf_path)
		media_box = reader.pages[0].mediabox
		return len(reader.pages), (round(float(media_box.width)), round(float(media_box.height)))

	@staticmethod
	def page(index: int, placement: Placement) -> dict[str, object]:
		""" Build the Reef page showing one slide of the PDF.

		Args:
			index     (int):       0-based slide number, selecting the frame of the generated item model.
			placement (Placement): Scale and offsets bringing the slide onto the screen.
		Returns:
			dict[str, object]: Content of data/<ns>/reef/page/<name>/<index>.json
		"""
		namespace: str = Mem.ctx.project_id
		page: dict[str, object] = {
			"sequence": [[{
				"type": "graphic",
				"model": f"{namespace}:reef/mini/{SLIDESHOW_NAME}",
				"components": {"minecraft:custom_model_data": {"floats": [index]}},
				"pos": [placement.offset_x, -placement.offset_y, 0],
				"scale": [placement.scale, placement.scale, 1],
			}]]
		}
		override: PageOverride | None = PAGE_OVERRIDES.get(index)
		if override is not None:
			page["commands"] = override.to_commands()
		return page

	@staticmethod
	def report(page_count: int, page_size: tuple[int, int], placement: Placement, stage: Stage) -> None:
		""" Say what the slides will look like in game, and complain about a border worth fixing.

		Args:
			page_count (int):               Number of slides found in the PDF.
			page_size  (tuple[int, int]):   Page width and height of the exported PDF, in points.
			placement  (Placement):         Scale and offsets applied to every slide.
			stage      (Stage):             Stage the panel is presented on.
		"""
		info(
			f"Fitted {page_count} slides of {page_size[0]}x{page_size[1]} pt onto {stage.display_name} "
			f"({stage.blocks_wide:g}x{stage.blocks_tall:g} blocks) at scale {placement.scale:.4g}"
		)
		if max(placement.offset_x / stage.blocks_wide, placement.offset_y / stage.blocks_tall) > MAX_MARGIN_RATIO:
			warning(
				f"The slides leave a {placement.offset_x:.2f}x{placement.offset_y:.2f} block border on the screen. "
				f"Export them at a {stage.page_width / stage.page_height:.3f} aspect ratio to fill it edge to edge."
			)

	@staticmethod
	def write() -> None:
		""" Rasterize the presentation and register it so a Reef remote can load it in game. """
		namespace: str = Mem.ctx.project_id
		pdf_path: Path = Path(Mem.ctx.directory) / SOURCE_PDF

		if not pdf_path.is_file():
			warning(f"'{SOURCE_PDF}' not found next to beet.yml, no slideshow was built")
			return

		# Read the slide count and page size straight from the PDF so nothing has to be kept in sync by hand
		page_count, page_size = ReefSlideshow.read_pdf(pdf_path)
		placement: Placement = Placement.fit(page_size, TARGET_STAGE)
		ReefSlideshow.report(page_count, page_size, placement, TARGET_STAGE)

		# One texture, model and item model entry per slide, at the resolution the PDF was exported with
		Mem.ctx.assets[ReefPdfAsset][f"{namespace}:{SLIDESHOW_NAME}"] = ReefPdfAsset(source_path=pdf_path)

		# One page per slide, each shrinking its graphic down to the stage screen
		slideshow: list[str] = []
		for index in range(page_count):
			page_id: str = f"{namespace}:{SLIDESHOW_NAME}/{index}"
			Mem.ctx.data[ReefPageData][page_id] = ReefPageData(json.dumps(ReefSlideshow.page(index, placement)))
			slideshow.append(page_id)
		Mem.ctx.data[ReefSlideshowData][f"{namespace}:{SLIDESHOW_NAME}"] = ReefSlideshowData(json.dumps(slideshow))

		# Reef only learns about the slideshow once this generated function has run
		write_load_file(f"function {namespace}:reef/register_namespace")
		info(f"Registered slideshow '{namespace}:{SLIDESHOW_NAME}' holding {page_count} slides")
