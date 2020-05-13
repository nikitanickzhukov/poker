from ..base.games import Game as BaseGame
from .streets import Preflop, Flop, Turn, River
from .hands import Identifier


class Game(BaseGame):
    street_classes = (Preflop, Flop, Turn, River)
    identifier_class = Identifier


__all__ = ('Game',)
