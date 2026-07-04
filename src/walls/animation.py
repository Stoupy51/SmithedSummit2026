""" Animation helpers for one wall: the arrow click "pop" and the page fade.

Pop: the clicked arrow snaps to ARROW_POP x its size immediately, then
pop_settle eases it back to normal one tick later. Three points matter:
 - one 'data merge' per step so the whole transform update lands atomically.
 - scale is a list of FLOATS: the values must carry the 'f' suffix, or the
   merge is dropped as a double/float type mismatch (nothing moves).
 - start_interpolation is ABSOLUTE game-time, not a delay: 0 is a tick in the
   distant past, so the window has already elapsed and the entity snaps. Use
   -1, which the game rewrites to the current tick = "interpolate from now".
   duration 0 + start -1 = an instant, applied snap.
 - the snap and ease-back land on separate ticks: the client interpolates
   from its last *rendered* transform, so a same-tick big->normal never pops.

Fade: driven manually, one opacity value per tick. The client interpolates
text_opacity as a raw *signed* byte, so it can't ramp invisible(~10)->opaque
(255/-1): the short numeric path runs the wrong way through the 0..3 "opaque"
band. So the page skips built-in opacity interpolation entirely - a per-wall
counter (holder in <ns>.fc) counts a phase down from FADE_TICKS to 0 and each
tick we write the exact opacity + background + translation for that frame.
"""

# Imports
from stewbeet import write_function

from .settings import (
	ARROW_POP,
	ARROW_POP_TICKS,
	ARROW_SCALE,
	BG_ALPHA_FULL,
	FADE_DROP,
	FADE_INTERP,
	FADE_TICKS,
	PAGE_ALPHA_FADED,
	PAGE_ALPHA_FULL,
)
from .wall import Wall

# The clicked arrow snaps to this absolute scale before easing back to ARROW_SCALE.
ARROW_POP_SCALE: float = round(ARROW_SCALE * ARROW_POP, 4)


# ── Arrow click feedback ("pop") ──────────────────────────────────────────────

def scale_merge(value: float, duration: int) -> str:
	""" data-merge SNBT setting scale (float list) + an interpolation of `duration` ticks. """
	scale: str = f"[{value}f,{value}f,{value}f]"
	return "{interpolation_duration:" + str(duration) + ",start_interpolation:-1,transformation:{scale:" + scale + "}}"


def pop_arrow_commands(wall: Wall, arrow_uuid: str) -> str:
	""" Commands snapping the clicked arrow to its popped size *now*, then letting
	pop_settle ease it back to normal one tick later (see the module docstring
	for why the snap and the ease-back must land on separate ticks). """
	return f"""# Click feedback: snap the clicked arrow to its popped size now, ease it back next tick
data merge entity {arrow_uuid} {scale_merge(ARROW_POP_SCALE, 0)}
schedule function {wall.function('pop_settle')} 2t replace"""


def write_pop_settle(wall: Wall) -> None:
	""" Write pop_settle: ease both arrows back to normal size (the un-clicked one
	is already there, so its interpolation is a no-op). One shared settle keeps
	rapid alternating clicks - which 'schedule ... replace' collapses to a single
	firing - correct. """
	write_function(wall.function("pop_settle"), f"""
# Ease both arrows back to normal size over {ARROW_POP_TICKS} ticks
# (the un-clicked arrow is already at normal size, so its interpolation is a no-op)
data merge entity {wall.left_arrow_uuid} {scale_merge(ARROW_SCALE, ARROW_POP_TICKS)}
data merge entity {wall.right_arrow_uuid} {scale_merge(ARROW_SCALE, ARROW_POP_TICKS)}
""", overwrite=True)


# ── Page fade (out -> swap -> in) ─────────────────────────────────────────────

def text_alpha(fraction: float) -> int:
	""" Unsigned text alpha for a fade frame. fraction 0..1 = faded..full. """
	return round(PAGE_ALPHA_FADED + (PAGE_ALPHA_FULL - PAGE_ALPHA_FADED) * fraction)


def page_frame_command(wall: Wall, opacity: int, bg_alpha: int, y: float, duration: int) -> str:
	""" One fade frame: unsigned alpha `opacity` (converted to the signed NBT
	byte), background alpha `bg_alpha` (ARGB, black), vertical translation `y`,
	smoothed over `duration` ticks. """
	signed_byte: int = opacity - 256 if opacity > 127 else opacity
	return (f"data merge entity {wall.page_uuid} "
		"{interpolation_duration:" + str(duration) + ",start_interpolation:-1"
		",text_opacity:" + str(signed_byte) + "b"
		",background:" + str(bg_alpha << 24) +
		",transformation:{translation:[0f," + f"{round(y, 4)}f" + ",0f]}}")


def phase_frames(wall: Wall, frames: list[tuple[int, float, float]]) -> list[str]:
	""" One 'apply when the fade counter == c' line per (c, fraction, y) frame.

	Each frame interpolates over FADE_INTERP ticks for smoothness; since we
	step one value per tick ourselves, every lerp stays between adjacent alpha
	values and never crosses the 0..3 opaque band the wrong way (the only snap
	is the reposition in fade_swap, which uses duration 0). """
	lines: list[str] = []
	for c, fraction, y in frames:
		frame: str = page_frame_command(wall, text_alpha(fraction), round(BG_ALPHA_FULL * fraction), y, FADE_INTERP)
		lines.append(f"execute if score {wall.holder} {wall.fade_objective} matches {c} run {frame}")
	return lines


def write_fade_direction(wall: Wall, direction: str, exit_y: float, entry_y: float) -> None:
	""" Write the three phases of one fade direction (down or up).

	`exit_y` is where the old text slides off to; `entry_y` is the opposite
	side the new text slides in from.
		fade_out_*:  counter F->0, text ramps full->invisible while sliding to exit_y.
		fade_swap_*: once invisible, swap the new page in (show) at entry_y, reset F.
		fade_in_*:   counter F->0, text ramps invisible->full while sliding entry_y->0.
	"""
	holder: str = wall.holder
	fcobj: str = wall.fade_objective
	F: int = FADE_TICKS

	out_lines: list[str] = [
		f"# Fade out ({direction}): while the counter ({holder} {fcobj}) ticks {F}->0, ramp the text",
		"# full->invisible and slide it towards its exit side, one exact frame per counter value",
	]
	out_lines += phase_frames(wall, [(c, c / F, exit_y * (F - c) / F) for c in range(F, -1, -1)])
	# At c==0 hand off to fade_swap via SCHEDULE, not an inline call: fade_swap
	# resets fc to F, and an inline call would let the `matches 1..` guards below
	# re-see fc=F and re-arm fade_out - looping fade_out and fade_in forever.
	out_lines += [
		"",
		"# Counter at 0: the text is invisible, hand off to fade_swap next tick (via schedule, NOT",
		"# an inline call: fade_swap resets the counter, which would re-arm the guards below)",
		f"execute if score {holder} {fcobj} matches 0 run schedule function {wall.function(f'fade_swap_{direction}')} 1t replace",
		"",
		"# Otherwise: re-run this function next tick and count down",
		f"execute if score {holder} {fcobj} matches 1.. run schedule function {wall.function(f'fade_out_{direction}')} 1t replace",
		f"execute if score {holder} {fcobj} matches 1.. run scoreboard players remove {holder} {fcobj} 1",
	]
	write_function(wall.function(f"fade_out_{direction}"), "\n".join(out_lines) + "\n", overwrite=True)

	# Reposition (still invisible) to the entry side; snap it (dur 0) so the text
	# doesn't visibly glide across from the exit side while it's being placed.
	write_function(wall.function(f"fade_swap_{direction}"), f"""
# The old text is now invisible: swap the new page in, then snap it (duration 0, still
# invisible) to its entry side so it doesn't visibly glide across from the exit side
function {wall.function('show')}
{page_frame_command(wall, PAGE_ALPHA_FADED, 0, entry_y, 0)}

# Re-arm the phase counter and start the fade-in next tick
scoreboard players set {holder} {fcobj} {F}
schedule function {wall.function(f'fade_in_{direction}')} 1t replace
""", overwrite=True)

	in_lines: list[str] = [
		f"# Fade in ({direction}): while the counter ({holder} {fcobj}) ticks {F}->0, ramp the new text",
		"# invisible->full while it slides from its entry side back to center",
	]
	in_lines += phase_frames(wall, [(c, (F - c) / F, entry_y * c / F) for c in range(F, -1, -1)])
	in_lines += [
		"",
		"# Re-run this function next tick and count down until the counter reaches 0",
		f"execute if score {holder} {fcobj} matches 1.. run schedule function {wall.function(f'fade_in_{direction}')} 1t replace",
		f"execute if score {holder} {fcobj} matches 1.. run scoreboard players remove {holder} {fcobj} 1",
	]
	write_function(wall.function(f"fade_in_{direction}"), "\n".join(in_lines) + "\n", overwrite=True)


def write_fade_functions(wall: Wall) -> None:
	""" Write both fade directions for this wall.

	Right arrow -> "down": the old text slides down, the new enters from above.
	Left arrow  -> "up":   the old text slides up,   the new enters from below. """
	write_fade_direction(wall, "down", -FADE_DROP, FADE_DROP)
	write_fade_direction(wall, "up", FADE_DROP, -FADE_DROP)


def clear_fade_commands(wall: Wall) -> str:
	""" Commands cancelling any fade chain still in flight for this wall (both
	directions, all three phases) so a fast second click can't leave two chains
	fighting over the counter. """
	return "\n".join(
		f"schedule clear {wall.function(f'fade_{phase}_{direction}')}"
		for direction in ("down", "up") for phase in ("out", "swap", "in"))

