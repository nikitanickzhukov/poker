from itertools import combinations

from ..base.hands import Hands as BaseHands, HighCard, OnePair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush
from .pockets import Pocket
from .boards import Board


class Hands(BaseHands):
    @classmethod
    def get_combs(cls, pocket:Pocket, board:Board) -> iter:
        cards = [ x for x in pocket ] + [ y for y in board ]
        cards.sort(key=lambda x: x.rank, reverse=True)
        return list(combinations(cards, cls.length))


__all__ = ('Hands', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush',)
