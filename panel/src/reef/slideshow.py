""" Turns the presentation PDF into a Reef slideshow.

Reef reads the in-game slide size straight from the PDF page size, so the export has to match the stage.
The page count is read from the PDF on every build, which means adding or removing slides needs no code change.
"""
# Imports
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pdf2image import pdfinfo_from_path
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

PAGE_SIZE_PATTERN: re.Pattern[str] = re.compile(r"([\d.]+) x ([\d.]+) pts")
""" Shape of the `Page size` field returned by poppler's pdfinfo, ex: "336 x 192 pts". """


# Classes
@dataclass(frozen=True)
class PageOverride:
	""" Commands Reef runs around one slide.

	Only commands are supported on purpose: reef 1.0.0b7 crashes on an override carrying
	anything other than exactly one element group, so the sequence field is left alone.
	"""

	on_load: list[str] = field(default_factory=list)
	""" Runs once when the slideshow is loaded onto a screen. """
	on_enter: list[str] = field(default_factory=list)
	""" Runs every time the slide is shown. """
	on_unload: list[str] = field(default_factory=list)
	""" Runs when the slideshow is cleared. """

	def to_page(self) -> dict[str, Any]:
		""" Convert to the partial Reef page that Reef merges into the generated slide.

		Returns:
			dict[str, Any]: Page holding only the command lists that are not empty.

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
	# Slide indexes are 0-based. Example, arming the tomatoes when the AI slide shows up:
	# 12: PageOverride(on_enter=["function stoupy_panel:tomato/enable"], on_unload=["function stoupy_panel:tomato/disable"]),
}
""" Per-slide commands. While empty, the slideshow compiles to a lighter Reef Mini definition. """


class ReefSlideshow:
	""" Build-time generation of the panel slideshow out of the presentation PDF. """

	@staticmethod
	def poppler_arguments() -> dict[str, str]:
		""" Tell pdf2image where poppler lives, reusing the path already configured for Reef.

		Returns:
			dict[str, str]: Keyword arguments for pdf2image, empty when poppler is on the PATH.
		"""
		pdf_options: dict[str, Any] = Mem.ctx.meta.get("reef", {}).get("pdf", {})
		poppler_path: str | None = pdf_options.get("poppler_path")
		return {"poppler_path": poppler_path} if poppler_path else {}

	@staticmethod
	def read_page_size(raw: str) -> tuple[int, int]:
		""" Parse poppler's `Page size` field into rounded points.

		Args:
			raw (str): Raw field, ex: "336 x 192 pts"
		Returns:
			tuple[int, int]: Page width and height in points.

		Examples:
			>>> ReefSlideshow.read_page_size("336 x 192 pts")
			(336, 192)
		"""
		match: re.Match[str] | None = PAGE_SIZE_PATTERN.match(raw)
		if match is None:
			raise ValueError(f"Could not read the page size of '{SOURCE_PDF}' out of '{raw}'")
		return round(float(match.group(1))), round(float(match.group(2)))

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
	def definition(page_count: int) -> dict[str, Any]:
		""" Build the `reef:pdf` special definition that compiles the PDF into a slideshow.

		Args:
			page_count (int): Number of slides found in the PDF.
		Returns:
			dict[str, Any]: Content of data/<ns>/reef/special/<name>.json
		"""
		namespace: str = Mem.ctx.project_id
		definition: dict[str, Any] = {
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
		pdf_info: dict[str, Any] = pdfinfo_from_path(str(pdf_path), **ReefSlideshow.poppler_arguments())
		page_count: int = int(pdf_info["Pages"])
		ReefSlideshow.check_page_size(ReefSlideshow.read_page_size(str(pdf_info["Page size"])), TARGET_STAGE)

		# One texture, model and item model entry per slide
		Mem.ctx.assets[ReefPdfAsset][f"{namespace}:{SLIDESHOW_NAME}"] = ReefPdfAsset(source_path=pdf_path)

		# Compile those slides into a slideshow the Reef remote can load
		Mem.ctx.data[ReefSpecialData][f"{namespace}:{SLIDESHOW_NAME}"] = ReefSpecialData(json.dumps(ReefSlideshow.definition(page_count)))

		# Reef only learns about the slideshow once this generated function has run
		write_load_file(f"function {namespace}:reef/register_namespace")
		info(f"Registered slideshow '{namespace}:{SLIDESHOW_NAME}' holding {page_count} slides")

