from itertools import combinations, product

from ..base import hands
from .pockets import Pocket
from .boards import Board


class HighCard(hands.HighCard):
    pass


class OnePair(hands.OnePair):
    pass


class TwoPair(hands.TwoPair):
    pass


class Trips(hands.Trips):
    pass


class Straight(hands.Straight):
    pass


class Flush(hands.Flush):
    pass


class FullHouse(hands.FullHouse):
    pass


class Quads(hands.Quads):
    pass


class StraightFlush(hands.StraightFlush):
    pass


class Hands(hands.Hands):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)
    pocket_comb_length = 2

    @classmethod
    def get_combs(cls, pocket:Pocket, board:Board) -> iter:
        pc = combinations(pocket, cls.pocket_comb_length)
        bc = combinations(board, cls.length - cls.pocket_comb_length)
        combs = [ sorted(x + y, reverse=True) for x, y in product(pc, bc) ]
        combs.sort(reverse=True)
        return combs


__all__ = ('Hands', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
