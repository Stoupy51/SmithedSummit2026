""" Turns the presentation PDF into a Reef slideshow.

Reef reads the in-game slide size straight from the PDF page size, so the export has to match the stage.
The page count is read from the PDF on every build, which means adding or removing slides needs no code change.
"""
# Imports
import json
from dataclasses import dataclass, field
from pathlib import Path

from pypdf import PdfReader
from stewbeet import Mem, write_load_file
from stouputils.print import info, warning

from reef.assets.pdf import ReefPdfAsset
from reef.data.special import ReefSpecialData

from .stages import POINTS_PER_BLOCK, TARGET_STAGE, Stage

# Constants
SOURCE_PDF: str = "How to Boost your Productivity.pdf"
""" Presentation export sitting next to beet.yml. Re-export over this file to update the slides. """

SLIDESHOW_NAME: str = "panel"
""" Path of the generated slideshow, loaded in game as `<namespace>:panel`. """


# Classes
@dataclass(frozen=True)
class PageOverride:
	""" Commands Reef runs around one slide.

	Only commands are supported on purpose: reef 1.0.0b7 crashes on an override carrying
	anything other than exactly one element group, so the sequence field is left alone.
	"""

	on_load: list[str] = field(default_factory=list[str])
	""" Runs once when the slideshow is loaded onto a screen. """
	on_enter: list[str] = field(default_factory=list[str])
	""" Runs every time the slide is shown. """
	on_unload: list[str] = field(default_factory=list[str])
	""" Runs when the slideshow is cleared. """

	def to_page(self) -> dict[str, object]:
		""" Convert to the partial Reef page that Reef merges into the generated slide.

		Returns:
			dict[str, object]: Page holding only the command lists that are not empty.

		Examples:
			>>> PageOverride(on_enter=["say hi"]).to_page()
			{'commands': {'on_enter': ['say hi']}}
		"""
		named_commands: tuple[tuple[str, list[str]], ...] = (
			("on_load",   self.on_load),
			("on_enter",  self.on_enter),
			("on_unload", self.on_unload),
		)
		return {"commands": {name: commands for name, commands in named_commands if commands}}


# Constants
PAGE_OVERRIDES: dict[int, PageOverride] = {
	# Slide indexes are 0-based. Example, handing out the tomatoes when the AI slide shows up:
	# 12: PageOverride(on_enter=["function stoupy_panel:tomato/give"], on_unload=["function stoupy_panel:tomato/clear"]),
}
""" Per-slide commands. While empty, the slideshow compiles to a lighter Reef Mini definition. """


class ReefSlideshow:
	""" Build-time generation of the panel slideshow out of the presentation PDF. """

	@staticmethod
	def read_pdf(pdf_path: Path) -> tuple[int, tuple[int, int]]:
		""" Read the slide count and the page size straight out of the presentation.

		The size is taken from the first page only, since Reef gives the whole slideshow
		the size of the PDF anyway.

		Args:
			pdf_path (Path): Presentation to inspect.
		Returns:
			tuple[int, tuple[int, int]]: Slide count, then page width and height in points.
		"""
		reader: PdfReader = PdfReader(pdf_path)
		media_box = reader.pages[0].mediabox
		return len(reader.pages), (round(float(media_box.width)), round(float(media_box.height)))

	@staticmethod
	def check_page_size(page_size: tuple[int, int], stage: Stage) -> None:
		""" Compare the export against the stage screen and explain the fix when they differ.

		Args:
			page_size (tuple[int, int]): Page width and height of the exported PDF, in points.
			stage     (Stage):           Stage the panel is presented on.
		"""
		if page_size == (stage.page_width, stage.page_height):
			info(f"Slides match {stage.display_name}: {stage.page_width}x{stage.page_height} pt -> {stage.blocks_wide:g}x{stage.blocks_tall:g} blocks")
			return

		width, height = page_size
		warning(
			f"'{SOURCE_PDF}' is {width}x{height} pt but {stage.display_name} expects {stage.page_width}x{stage.page_height} pt. "
			f"Reef would render a {width / POINTS_PER_BLOCK:g}x{height / POINTS_PER_BLOCK:g} block screen "
			f"instead of {stage.blocks_wide:g}x{stage.blocks_tall:g}. "
			f"Re-export the presentation with a custom page size of {stage.page_width}x{stage.page_height} pt."
		)

	@staticmethod
	def definition(page_count: int) -> dict[str, object]:
		""" Build the `reef:pdf` special definition that compiles the PDF into a slideshow.

		Args:
			page_count (int): Number of slides found in the PDF.
		Returns:
			dict[str, object]: Content of data/<ns>/reef/special/<name>.json
		"""
		namespace: str = Mem.ctx.project_id
		definition: dict[str, object] = {
			"type": "reef:pdf",
			"pdf": f"{namespace}:{SLIDESHOW_NAME}",
			"page_count": page_count,
		}
		if PAGE_OVERRIDES:
			definition["overrides"] = {str(index): override.to_page() for index, override in sorted(PAGE_OVERRIDES.items())}
		return definition

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
		ReefSlideshow.check_page_size(page_size, TARGET_STAGE)

		# One texture, model and item model entry per slide
		Mem.ctx.assets[ReefPdfAsset][f"{namespace}:{SLIDESHOW_NAME}"] = ReefPdfAsset(source_path=pdf_path)

		# Compile those slides into a slideshow the Reef remote can load
		Mem.ctx.data[ReefSpecialData][f"{namespace}:{SLIDESHOW_NAME}"] = ReefSpecialData(json.dumps(ReefSlideshow.definition(page_count)))

		# Reef only learns about the slideshow once this generated function has run
		write_load_file(f"function {namespace}:reef/register_namespace")
		info(f"Registered slideshow '{namespace}:{SLIDESHOW_NAME}' holding {page_count} slides")

