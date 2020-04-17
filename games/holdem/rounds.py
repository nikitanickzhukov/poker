from cards import StandardDeck
from ..base import Round as BaseRound
from .boards import Board
from .hands import HandIdentifier


class Round(BaseRound):
    deck_class = StandardDeck
    board_class = Board
    hand_class = HandIdentifier


__all__ = ('Round',)
