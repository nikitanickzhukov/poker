from ..base import Round
from .street import Preflop, Flop, Turn, River
from .hand import Identifier


class NoLimitHoldemRound(Round):
    street_classes = (Preflop, Flop, Turn, River)
    identifier_class = Identifier


__all__ = ('NoLimitHoldemRound',)
