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

    @classmethod
    def identify(cls, comb:list) -> None:
        return None

    @property
    def weight(self):
        return [self.hand_weight,]

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


class Hands(ABC):
    length = 0
    hand_classes = ()

    @classmethod
    def identify(cls, pocket:Pocket, board:Board) -> Hand:
        cards = cls.get_cards(pocket, board)
        combs = cls.get_combs(cards)

        for item in cls.hand_classes:
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
