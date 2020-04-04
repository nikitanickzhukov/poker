from cards import StandardDeck
from ..base import Round as BaseRound
from .pockets import Pocket
from .boards import Board
from .hands import HandIdentifier


class Round(BaseRound):
    deck_class = StandardDeck
    pocket_class = Pocket
    board_class = Board
    identifier_class = HandIdentifier


__all__ = ('Round',)
