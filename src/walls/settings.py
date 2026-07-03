""" Tunable geometry, scale and animation settings for the presentation walls.

Every constant here is safe to tweak in-world: geometry offsets are expressed in a
wall's local frame (caret: ^left ^up ^forward, where "forward" is the way each
Zone.rotation faces), scales are display-entity transformation scales, and the
animation values drive the arrow "pop" click feedback and the page fade transition.
"""

# ── Geometry (local-frame offsets, in blocks) ─────────────────────────────────
WALL_FWD: float = -0.45     # push displays just in front of the wall face
PAGE_UP: float = 1.2        # page text vertical offset from the anchor block
TITLE_UP: float = 3.0       # title sits above the wall
ARROW_UP: float = 0.5       # arrows vertical offset (same height as the page)
ARROW_OUT: float = 1.0      # horizontal distance from center to each arrow
INT_W: float = 0.9          # interaction hitbox width
INT_H: float = 0.9          # interaction hitbox height
LINK_INT: float = 0.75      # "Open link" interaction hitbox size (0 on pages with no link)

# ── Display scales ────────────────────────────────────────────────────────────
PAGE_SCALE: float = 0.60    # text_display scale for pages
TITLE_SCALE: float = 0.9    # text_display scale for the title
ARROW_SCALE: float = 1.0    # item_display scale for the arrows
LINK_SCALE: float = 0.5     # text_display scale for the centered "Open link" prompt

# ── Arrow click feedback ("pop") ──────────────────────────────────────────────
ARROW_POP: float = 1.25     # clicked arrow snaps to this multiple of ARROW_SCALE, then eases back
ARROW_POP_TICKS: int = 8    # ticks for the clicked arrow to ease from the popped size back to normal

# ── Page fade transition ──────────────────────────────────────────────────────
FADE_TICKS: int = 2         # ticks per page fade phase (out, then in)
FADE_DROP: float = 0.15     # vertical slide distance (blocks) of the page text during a fade
FADE_INTERP: int = 4        # per-frame interpolation_duration (ticks) that smooths between frames

# text_opacity byte bands (unsigned alpha): 0..3 render fully opaque (avoid!), 4..26 are
# invisible, 27..255 ramp faint->opaque. We drive opacity ourselves one value per tick
# (the client's byte interpolation lerps the raw *signed* byte, which can't ramp
# invisible->255), so these are just the endpoints of that manual ramp.
PAGE_ALPHA_FULL: int = 255      # fully opaque
PAGE_ALPHA_FADED: int = 10      # invisible (inside the 4..26 band, clear of the 0..3 quirk)
BG_ALPHA_FULL: int = 64         # default page background alpha (0x40 of 0x40000000, black)
