from typing import Union
from abc import ABC
import random

from .ranks import Rank
from .suits import Suit
from .cards import Card


class Deck(ABC):
    """
    Representation of abstract deck
    """

    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._items)

    def __str__(self) -> str:
        return str([ str(x) for x in self._items ])

    def __bool__(self) -> bool:
        return bool(self._items)

    def __eq__(self, other:'Deck') -> bool:
        return self._items == other._items

    def __ne__(self, other:'Deck') -> bool:
        return self._items != other._items

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

    def __delitem__(self, key:Union[int, str]) -> None:
        if isinstance(key, int):
            del self._items[key]
        elif isinstance(key, str):
            ok = False
            for i in range(len(self._items)):
                if self._items[i].code == key:
                    del self._items[i]
                    ok = True
                    break
            if not ok:
                raise KeyError('Card {} is not found'.format(key))
        else:
            raise AssertionError('Wrong key type')

    def shuffle(self) -> None:
        random.shuffle(self._items)

    def push(self, *args) -> None:
        assert all(isinstance(x, Card) for x in args), 'Deck cannot contain non-card items'
        assert all(x not in self._items for x in args), 'Deck already contains such card(s)'
        self._items.extend(args)

    def pop(self) -> Card:
        return self._items.pop()

    def unshift(self, *args) -> None:
        assert all(isinstance(x, Card) for x in args), 'Deck cannot contain non-card items'
        assert all(x not in self._items for x in args), 'Deck already contains such card(s)'
        self._items[0:0] = args

    def shift(self) -> Card:
        return self._items.pop(0)


suits = (
    Suit(code='s', name='spades', weight=1),
    Suit(code='h', name='hearts', weight=1),
    Suit(code='d', name='diamonds', weight=1),
    Suit(code='c', name='clubs', weight=1),
)
ranks = (
    Rank(code='A', name='Ace', weight=14),
    Rank(code='2', name='Deuce', weight=2),
    Rank(code='3', name='Trey', weight=3),
    Rank(code='4', name='Four', weight=4),
    Rank(code='5', name='Five', weight=5),
    Rank(code='6', name='Six', weight=6),
    Rank(code='7', name='Seven', weight=7),
    Rank(code='8', name='Eight', weight=8),
    Rank(code='9', name='Nine', weight=9),
    Rank(code='T', name='Ten', weight=10),
    Rank(code='J', name='Jack', weight=11),
    Rank(code='Q', name='Queen', weight=12),
    Rank(code='K', name='King', weight=13),
)
cards = [ Card(rank=r, suit=s) for s in suits for r in ranks ]


class StandardDeck(Deck):
    """
    Standard 52-card deck
    """

    def __init__(self) -> None:
        super().__init__()
        self._items = cards.copy()


__all__ = ('Deck', 'StandardDeck', 'suits', 'ranks', 'cards')
