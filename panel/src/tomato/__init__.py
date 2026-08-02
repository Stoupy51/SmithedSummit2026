""" Throwable tomatoes for the AI section of the panel.

Right clicking a tomato launches it, Bookshelf's move module flies it, and the first block it
touches bursts it into redstone block debris. Tomatoes always fly, so the only two controls are
`<ns>:tomato/give` and `<ns>:tomato/clear`, the latter doubling as the kill switch.
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
