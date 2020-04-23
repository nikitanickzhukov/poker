from ..base import Round as BaseRound
from .boards import Board
from .pockets import Pocket
from .hands import HandIdentifier


class Round(BaseRound):
    board_class = Board
    pocket_class = Pocket
    hand_class = HandIdentifier


__all__ = ('Round',)
