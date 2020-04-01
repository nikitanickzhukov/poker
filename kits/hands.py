from typing import Union, Optional
from abc import ABC

from cards import Card
from .pockets import Pocket
from .boards import Board


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
    def weight(self) -> None:
        return (self.hand_weight,)


class HandIdentifier(ABC):
    length = 0
    hand_classes = ()

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
