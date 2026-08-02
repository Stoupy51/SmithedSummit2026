""" Reef slideshow generation, see REEF.md for the library reference. """
# Imports
from beet import Context

from .slideshow import ReefSlideshow


# Main entry point
def beet_default(ctx: Context) -> None:
	""" Rasterize the presentation PDF and register it as a Reef slideshow. """
	ReefSlideshow.write()
