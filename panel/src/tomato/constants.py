""" Tunables and shared names for the throwable tomatoes.

Everything the audience can feel (how far a tomato flies, how long it lives, how many they get)
lives here so the panel can be balanced without touching the command generation.
"""

# Constants
TOMATO_ITEM: str = "tomato"
""" Item id registered in src/definitions/additions.py. """

THROW_SPEED: int = 1800
""" Initial speed in thousandths of a block per tick, so 900 is 0.9 block per tick. """

GRAVITY: int = 35
""" Pull removed from the vertical velocity every tick, in thousandths of a block per tick. """

LIFETIME: int = 200
""" Ticks a tomato flies before splatting on its own, so a throw into the void never litters the stage. """

TOMATOES_PER_PLAYER: int = 8
""" How many tomatoes `<ns>:tomato/give` hands out to each player. """

SPLAT_PARTICLES: int = 60
""" Redstone block particles spawned on impact. """

TOMATO_TAG: str = "tomato"
""" Suffix of the entity tag marking a flying tomato, prefixed with the namespace at write time. """

USED_TAG: str = "tomato.used"
""" Suffix of the tag debouncing the right click, so holding the button throws only once. """

THROWER_TAG: str = "tomato.thrower"
""" Suffix of the short lived tag letting a freshly summoned tomato find who threw it. """
