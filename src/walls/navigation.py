""" Navigation functions for one wall: next and prev.

Each one: advance/rewind the page score, play the click sound, pop the clicked
arrow, then kick off the page fade (fade_out defers the text swap to fade_swap,
so the old text stays put until it has faded away). A no-op at the boundary
(already on the last/first page) returns before doing anything, so a dead-end
click neither animates nor interrupts an ongoing fade. The boundary guard also
makes a wrap-around clamp unnecessary.
"""

# Imports
from stewbeet import write_function

from .animation import clear_fade_commands, pop_arrow_commands
from .settings import FADE_TICKS
from .wall import Wall


def write_navigation_functions(wall: Wall) -> None:
	""" Write next (right arrow, fades down) and prev (left arrow, fades up). """
	holder: str = wall.holder
	obj: str = wall.page_objective

	write_function(wall.function("next"), f"""
# Click sound for nearby players
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.5

# Boundary guard: already on the last page (the right arrow is grayed), do nothing
execute if score {holder} {obj} matches {wall.page_count - 1}.. run return 0

# Cancel any fade chain still in flight so a fast second click can't leave two running
{clear_fade_commands(wall)}

# Advance the page index (the text swap itself happens later, in fade_swap)
scoreboard players add {holder} {obj} 1

{pop_arrow_commands(wall, wall.right_arrow_uuid)}

# Kick off the page fade: arm the phase counter and run the first fade-out frame now
scoreboard players set {holder} {wall.fade_objective} {FADE_TICKS}
function {wall.function('fade_out_down')}
""", overwrite=True)

	write_function(wall.function("prev"), f"""
# Click sound for nearby players (slightly lower pitch than next)
playsound minecraft:ui.button.click block @a[distance=..12] ~ ~ ~ 0.7 1.2

# Boundary guard: already on the first page (the left arrow is grayed), do nothing
execute if score {holder} {obj} matches ..0 run return 0

# Cancel any fade chain still in flight so a fast second click can't leave two running
{clear_fade_commands(wall)}

# Rewind the page index (the text swap itself happens later, in fade_swap)
scoreboard players remove {holder} {obj} 1

{pop_arrow_commands(wall, wall.left_arrow_uuid)}

# Kick off the page fade: arm the phase counter and run the first fade-out frame now
scoreboard players set {holder} {wall.fade_objective} {FADE_TICKS}
function {wall.function('fade_out_up')}
""", overwrite=True)

