from abc import ABC

from .kits import Kit
from .streets import Flop, Turn, River


class HoldemBoard(Kit):
    street_classes = (Flop, Turn, River,)

class OmahaBoard(Kit):
    street_classes = (Flop, Turn, River,)
