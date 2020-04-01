from abc import ABC
from typing import Union, Optional

from cards import Card, ranks
from .pockets import Pocket
from .boards import Board

min_rank = min(ranks)
max_rank = max(ranks)


class Hand(ABC):
    hand_weight = 0
    first_is_best = False

    def __init__(self, *args) -> None:
        assert all(isinstance(x, Card) for x in args), 'Hand cannot contain non-card items'
        self._items = args

    def __eq__(self, other:'Hand') -> bool:
        return self.__class__ == other.__class__ and self._items == other._items

    def __ne__(self, other:'Hand') -> bool:
        return self.__class__ != other.__class__ or self._items != other._items

    def __gt__(self, other:'Hand') -> bool:
        return self.weight > other.weight

    def __ge__(self, other:'Hand') -> bool:
        return self.weight >= other.weight

    def __lt__(self, other:'Hand') -> bool:
        return self.weight < other.weight

    def __le__(self, other:'Hand') -> bool:
        return self.weight <= other.weight

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, key:Union[int, str]) -> Card:
        if isinstance(key, (int, slice)):
            return self._items[key]
        elif isinstance(key, str):
            for item in self._items:
                if item.code == key:
                    return item
            raise KeyError('Card {} is not found'.format(key))
        else:
            raise AssertionError('Wrong key type')

    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        return True

    @classmethod
    def identify(cls, comb:tuple) -> 'Hand':
        return cls(*comb)

    @property
    def weight(self) -> tuple:
        return (self.hand_weight, *[ x.rank.weight for x in self._items ])


class HighCard(Hand):
    hand_weight = 1
    first_is_best = True

    def __repr__(self) -> str:
        return 'High card: {}, kickers: {}'.format(
                   self._items[0].rank.__repr__(),
                   ', '.join([ x.rank.__repr__() for x in self._items[1:] ]),
               )

    @classmethod
    def identify(cls, comb:tuple) -> 'HighCard':
        return cls(*comb)


class OnePair(Hand):
    hand_weight = 2
    first_is_best = True

    def __repr__(self) -> str:
        return 'One pair: {}s, kickers: {}'.format(
                   self._items[0].rank.__repr__(),
                   ', '.join([ x.rank.__repr__() for x in self._items[2:] ]),
               )

    @classmethod
    def identify(cls, comb:tuple) -> Optional['OnePair']:
        pair = None
        for i in range(len(comb) - 1):
            if comb[i].rank == comb[i + 1].rank:
                pair = list(comb[i:i + 2])
                break
        if pair:
            kickers = [ x for x in comb if x not in pair ]
            return cls(*(pair + kickers))
        return None


class TwoPair(Hand):
    hand_weight = 3
    first_is_best = True

    def __repr__(self) -> str:
        return 'Two pair: {}s and {}s, kicker: {}'.format(
                   self._items[0].rank.__repr__(),
                   self._items[2].rank.__repr__(),
                   self._items[4].rank.__repr__(),
               )

    @classmethod
    def identify(cls, comb:tuple) -> Optional['TwoPair']:
        pair1 = None
        pair2 = None
        for i in range(len(comb) - 1):
            if comb[i].rank == comb[i + 1].rank:
                if pair1 is None:
                    pair1 = list(comb[i:i + 2])
                elif pair2 is None:
                    pair2 = list(comb[i:i + 2])
                    break
        if pair1 and pair2:
            pairs = pair1 + pair2
            kickers = [ x for x in comb if x not in pairs ]
            return cls(*(pairs + kickers))
        return None


class Trips(Hand):
    hand_weight = 4
    first_is_best = True

    def __repr__(self) -> str:
        return 'Three of a kind: {}s, kickers: {}'.format(
                   self._items[0].rank.__repr__(),
                   ', '.join([ x.rank.__repr__() for x in self._items[3:] ]),
               )

    @classmethod
    def identify(cls, comb:tuple) -> Optional['Trips']:
        three = None
        for i in range(len(comb) - 2):
            if comb[i].rank == comb[i + 1].rank == comb[i + 2].rank:
                three = list(comb[i:i + 3])
                break
        if three:
            kickers = [ x for x in comb if x not in three ]
            return cls(*(three + kickers))
        return None


class Straight(Hand):
    hand_weight = 5
    first_is_best = False

    def __repr__(self) -> str:
        return '%s-high straight'.format(self._items[0].rank.__repr__())

    @classmethod
    def identify(cls, comb:tuple) -> Optional['Straight']:
        ok = True
        # Looking for a sequence Xabcd with any X
        for i in range(1, len(comb) - 1):
            if comb[i].rank.weight != comb[i + 1].rank.weight + 1:
                ok = False
                break
        if ok:
            if comb[0].rank.weight == comb[1].rank.weight + 1:
                # Standard straight: 98765 etc.
                return cls(*comb)
            elif comb[0].rank == max_rank and comb[4].rank == min_rank:
                # Wheel straight: 5432A
                return cls(*comb[1:], comb[0])
        return None


class Flush(Hand):
    hand_weight = 6
    first_is_best = True

    def __repr__(self) -> str:
        return '%s-high flush, %s'.format(
                   self._items[0].rank.__repr__(),
                   ', '.join([ x.rank.__repr__() for x in self._items[1:] ])
               )

    @classmethod
    def identify(cls, comb:tuple) -> Optional['Flush']:
        ok = True
        for i in range(len(comb) - 1):
            if comb[i].suit != comb[i + 1].suit:
                ok = False
                break
        if ok:
            return cls(*comb)
        return None


class FullHouse(Hand):
    hand_weight = 7
    first_is_best = True

    def __repr__(self) -> str:
        return 'Full house: {}s over {}s'.format(
                   self._items[0].rank.__repr__(),
                   self._items[3].rank.__repr__(),
               )

    @classmethod
    def identify(cls, comb:tuple) -> Optional['FullHouse']:
        trips = Trips.identify(comb)
        if trips:
            if trips[3].rank == trips[4].rank:
                return cls(*trips)
        return None


class Quads(Hand):
    hand_weight = 8
    first_is_best = True

    def __repr__(self) -> str:
        return 'Four of a kind: {}s, kicker: {}'.format(
                   self._items[0].rank.__repr__(),
                   self._items[4].rank.__repr__(),
               )

    @classmethod
    def identify(cls, comb:tuple) -> Optional['Quads']:
        trips = Trips.identify(comb)
        if trips:
            if trips[3].rank == trips[0].rank:
                return cls(*trips)
            elif trips[4].rank == trips[0].rank:
                return cls(*trips[0:3], trips[4], trips[3])
        return None


class StraightFlush(Hand):
    hand_weight = 9
    first_is_best = False

    def __repr__(self) -> str:
        if self._items[0].rank == max_rank:
            return 'Royal flush'
        return '%s-high straight flush'.format(self._items[0].rank.__repr__())

    @classmethod
    def identify(cls, comb:tuple) -> Optional['StraightFlush']:
        if Flush.identify(comb):
            straight = Straight.identify(comb)
            if straight:
                return cls(*straight)
        return None


class HandIdentifier(ABC):
    length = 5
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)

    def __init__(self, pocket:Pocket, board:Board) -> None:
        assert isinstance(pocket, Pocket), 'Pocket cannot be a non-pocket instance'
        assert isinstance(board, Board), 'Board cannot be a non-board instance'
        self._pocket = pocket
        self._board = board

    def identify(self) -> Optional[Hand]:
        for HandClass in self.hand_classes:
            if not HandClass.precheck(self.pocket, self.board):
                continue

            best_hand = None
            for comb in self._get_combs():
                hand = HandClass.identify(comb)
                if hand:
                    if HandClass.first_is_best:
                        best_hand = hand
                        break
                    elif not best_hand or hand > best_hand:
                        best_hand = hand
            if best_hand:
                return best_hand

        return None

    def _get_combs(self) -> iter:
        while False:
            yield

    @property
    def pocket(self):
        return self._pocket

    @property
    def board(self):
        return self._board


__all__ = ('Hand', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush', 'HandIdentifier')
