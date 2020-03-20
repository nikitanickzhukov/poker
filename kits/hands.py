from typing import Union
from abc import ABC
from itertools import combinations

from cards import Card
from .pockets import Pocket
from .boards import Board


class Hand(ABC):
    hand_weight = 0
    first_is_best = False

    def __init__(self, *args) -> None:
        assert all([ isinstance(x, Card) for x in args ]), 'Hand cannot contain non-card items'
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
        if isinstance(key, (int, slice,)):
            return self._items[key]
        elif isinstance(key, str):
            for item in self._items:
                if item.code == key:
                    return item
            raise KeyError('Card %s is not found' % (key,))
        else:
            raise TypeError('Wrong key type')

    @classmethod
    def precheck(cls, pocket:Pocket, board:Board) -> bool:
        return False

    @classmethod
    def identify(cls, comb:list) -> None:
        return None

    @property
    def weight(self):
        return [self.hand_weight,]


class Hands(ABC):
    length = 0
    hand_classes = ()

    @classmethod
    def identify(cls, pocket:Pocket, board:Board) -> Hand:
        cards = cls.get_cards(pocket, board)
        combs = cls.get_combs(cards)

        for item in cls.hand_classes:
            if not item.precheck(pocket, board, cards):
                continue

            best_hand = None
            for comb in combs:
                hand = item.identify(list(comb))
                if hand:
                    if item.first_is_best:
                        return hand
                    elif not best_hand or hand > best_hand:
                        best_hand = hand
            if best_hand:
                return best_hand
        raise Exception('Hand is not identified')

    @classmethod
    def get_cards(cls, pocket:Pocket, board:Board) -> list:
        raise NotImplementedError('Must be implemented')

    @classmethod
    def get_combs(cls, cards:list) -> iter:
        return list(combinations(cards, cls.length))
