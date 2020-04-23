from cards import StandardDeck
from ..base import Round as BaseRound
from .boards import Board
from .pockets import Pocket
from .dealers import Dealer
from .hands import HandIdentifier


class Round(BaseRound):
    deck_class = StandardDeck
    board_class = Board
    pocket_class = Pocket
    dealer_class = Dealer
    hand_class = HandIdentifier


__all__ = ('Round',)
