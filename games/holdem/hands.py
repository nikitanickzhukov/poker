from itertools import combinations
from collections import Counter

from cards import ranks
from ..base import hands
from .pockets import Pocket
from .boards import Board


min_rank = min(ranks)
max_rank = max(ranks)


class HighCard(hands.HighCard):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        return True


class OnePair(hands.OnePair):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain at leat 2 cards of one rank
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        count = Counter(ranks)
        most_common = count.most_common(1)
        return most_common[0][1] >= 2


class TwoPair(hands.TwoPair):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain
        # at least 2 cards of one rank and 2 cards of another one
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        count = Counter(ranks)
        most_common = count.most_common(2)
        return most_common[0][1] >= 2 and most_common[1][1] >= 2


class Trips(hands.Trips):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain at least 3 cards of one rank
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        count = Counter(ranks)
        most_common = count.most_common(1)
        return most_common[0][1] >= 3


class Straight(hands.Straight):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain at least 5 ordered cards (including wheel)
        ranks = sorted(set([ x.rank for x in pocket ] + [ y.rank for y in board ]), reverse=True)

        cur_str = [ranks[0]]
        max_str = []
        for i in range(1, len(ranks)):
            if ranks[i].weight == ranks[i - 1].weight - 1:
                cur_str.append(ranks[i])
            else:
                if len(cur_str) > len(max_str):
                    max_str = cur_str
                cur_str = [ranks[i]]
        if len(cur_str) > len(max_str):
            max_str = cur_str

        if max_str[-1] == min_rank and max_rank in ranks:
            # Wheel straight is found
            max_str.append(max_rank)

        if len(max_str) >= 5:
            return True
        return False

class Flush(hands.Flush):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain at least 5 cards of one suit
        suits = [ x.suit for x in pocket ] + [ y.suit for y in board ]
        count = Counter(suits)
        most_common = count.most_common(1)
        return most_common[0][1] >= 5


class FullHouse(hands.FullHouse):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain
        # at least 3 cards of one rank and 2 cards of another one
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        count = Counter(ranks)
        most_common = count.most_common(2)
        return most_common[0][1] >= 3 and most_common[1][1] >= 2


class Quads(hands.Quads):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        # Checking if pocket and board contain at least 4 cards of one rank
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        count = Counter(ranks)
        most_common = count.most_common(1)
        return most_common[0][1] >= 4


class StraightFlush(hands.StraightFlush):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        return Flush.precheck(pocket, board) and Straight.precheck(pocket, board)


class HandIdentifier(hands.HandIdentifier):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)

    def get_combs(self) -> iter:
        if not hasattr(self, '__comb_list'):
            self.__comb_list = []
        if not hasattr(self, '__comb_iter'):
            cards = sorted([*self.pocket] + [*self.board], key=lambda x: x.rank, reverse=True)
            self.__comb_iter = combinations(cards, self.length)

        for comb in self.__comb_list:
            yield comb
        for comb in self.__comb_iter:
            self.__comb_list.append(comb)
            yield comb

__all__ = ('HandIdentifier', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
