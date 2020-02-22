from abc import ABC

from .kits import Kit
from .streets import HoldemPreflop, OmahaPreflop


class HoldemHand(Kit):
    street_classes = (HoldemPreflop,)

class OmahaHand(Kit):
    street_classes = (OmahaPreflop,)
