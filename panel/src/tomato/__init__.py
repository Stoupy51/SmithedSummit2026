""" Throwable tomatoes for the AI section of the panel.

Right clicking a tomato launches it, Bookshelf's move module flies it, and the first block it
touches bursts it into redstone block debris. `<ns>:tomato/disable` is the kill switch.
"""
# Imports
from beet import Context

from .controls import TomatoControls
from .flight import TomatoFlight
from .throw import TomatoThrow


# Main entry point
def beet_default(ctx: Context) -> None:
	""" Write every function backing the throwable tomatoes. """
	TomatoThrow.write()
	TomatoFlight.write()
	TomatoControls.write()
