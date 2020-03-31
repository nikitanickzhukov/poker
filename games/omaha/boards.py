from kits import Board as BaseBoard
from .streets import Flop, Turn, River


class Board(BaseBoard):
    street_classes = (Flop, Turn, River)


__all__ = ('Board',)
