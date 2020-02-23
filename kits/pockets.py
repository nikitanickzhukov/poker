from abc import ABC

from .kits import Kit
from .streets import HoldemPreflop, OmahaPreflop


class HoldemPocket(Kit):
    street_classes = (HoldemPreflop,)

class OmahaPocket(Kit):
    street_classes = (OmahaPreflop,)
