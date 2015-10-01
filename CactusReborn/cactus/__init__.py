"""
__init__.py (./cactus)

__init__ serves an an import tool, taking away the need
to import every individual function and class in a Cactus
project. Even though wildcard imports are generally against
the general accepted style, in this case we don't want to
type out every single name, from each individual file.
"""
from .location import *
from .game_flowchart import *
from .main_game import *
from .player import *