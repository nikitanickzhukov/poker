from itertools import combinations, product

from ..base.hands import Hands as BaseHands, HighCard, OnePair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush
from .pockets import Pocket
from .boards import Board


class Hands(BaseHands):
    pocket_comb_length = 2

    @classmethod
    def get_combs(cls, pocket:Pocket, board:Board) -> iter:
        pc = combinations(pocket, cls.pocket_comb_length)
        bc = combinations(board, cls.length - cls.pocket_comb_length)
        combs = [ sorted(x + y, reverse=True) for x, y in product(pc, bc) ]
        combs.sort(reverse=True)
        return combs


__all__ = ('Hands', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
