from itertools import combinations, product
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
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        counter = Counter(ranks)
        for rank, count in counter.most_common(1):
            if count >= 2:
                return True
            else:
                break
        return False


class TwoPair(hands.TwoPair):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        counter = Counter(ranks)
        groups = []
        for rank, count in counter.most_common(4):
            if count >= 2:
                groups.append(rank)
            else:
                break
        pocket_count = len([ True for x in pocket if x.rank in groups ])
        if pocket_count >= 1:
            board_count = len([ True for x in board if x.rank in groups ])
            if board_count >= 2:
                return True
        return False


class Trips(hands.Trips):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        counter = Counter(ranks)
        for rank, count in counter.most_common(3):
            if count >= 3:
                pocket_count = len([ True for x in pocket if x.rank == rank ])
                if count - pocket_count >= 1:
                    return True
            else:
                break
        return False


class Straight(hands.Straight):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        ranks = sorted(set([ x.rank for x in pocket ] + [ y.rank for y in board ]), reverse=True)

        cur_seq = [ranks[0]]
        all_seq = []
        for i in range(1, len(ranks)):
            if ranks[i].weight == ranks[i - 1].weight - 1:
                cur_seq.append(ranks[i])
            else:
                if len(cur_seq) >= 4:
                    all_seq.append(cur_seq)
                cur_seq = [ranks[i]]
        if len(cur_seq) >= 4:
            all_seq.append(cur_seq)

        for seq in all_seq:
            if seq[-1] == min_rank and max_rank in ranks:
                # Wheel straight is found
                seq.append(max_rank)

        all_seq = [ x for x in all_seq if len(x) >= 5 ]

        for seq in all_seq:
            pocket_count = len(set([ x.rank for x in pocket if x.rank in seq ]))
            if pocket_count >= 2:
                board_count = len(set([ x.rank for x in board if x.rank in seq ]))
                if board_count >= 3:
                    return True
        return False


class Flush(hands.Flush):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        suits = [ x.suit for x in pocket ] + [ y.suit for y in board ]
        counter = Counter(suits)
        for suit, count in counter.most_common(1):
            if count >= 5:
                pocket_count = len([ True for x in pocket if x.suit == suit ])
                if pocket_count >= 2 and count - pocket_count >= 3:
                    return True
            else:
                break
        return False


class FullHouse(hands.FullHouse):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        counter = Counter(ranks)
        groups = []
        for rank, count in counter.most_common():
            if count >= 3:
                groups.append(rank)
            elif groups and count >= 2:
                groups.append(rank)
            else:
                break
        if len(groups) >= 2:
            pocket_count = len([ True for x in pocket if x.rank in groups ])
            if pocket_count >= 2:
                board_count = len([ True for x in board if x.rank in groups ])
                if board_count >= 3:
                    return True
        return False


class Quads(hands.Quads):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        ranks = [ x.rank for x in pocket ] + [ y.rank for y in board ]
        counter = Counter(ranks)
        for rank, count in counter.most_common(2):
            if count >= 4:
                pocket_count = len([ True for x in pocket if x.rank == rank ])
                if count - pocket_count >= 2:
                    return True
            else:
                break
        return False


class StraightFlush(hands.StraightFlush):
    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        return Flush.precheck(pocket, board) and Straight.precheck(pocket, board)


class HandIdentifier(hands.HandIdentifier):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)
    pocket_comb_length = 2

    def get_combs(self) -> iter:
        if not hasattr(self, '__comb_list'):
            self.__comb_list = []
        if not hasattr(self, '__comb_iter'):
            pc = combinations(self.pocket, self.pocket_comb_length)
            bc = combinations(self.board, self.length - self.pocket_comb_length)
            self.__comb_iter = sorted([ sorted(x + y, reverse=True) for x, y in product(pc, bc) ], reverse=True)

        for comb in self.__comb_list:
            yield comb
        for comb in self.__comb_iter:
            self.__comb_list.append(comb)
            yield comb


__all__ = ('HandIdentifier', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
