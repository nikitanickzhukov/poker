from abc import ABC

from .kits import Kit
from .streets import HoldemPreflop, OmahaPreflop


class HoldemHand(Kit):
    _street_classes = (HoldemPreflop,)

class OmahaHand(Kit):
    _street_classes = (OmahaPreflop,)
