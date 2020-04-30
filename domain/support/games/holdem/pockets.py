from ..base import Pocket as BasePocket
from .streets import Preflop


class Pocket(BasePocket):
    street_classes = (Preflop,)


__all__ = ('Pocket',)
