from abc import ABC
import random

from cards import Rank, Suit, Card


class Deck(ABC):
    """
    Representation of abstract deck
    """

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

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

    def __getitem__(self, idx:int) -> Card:
        return self._items[idx]

    def __delitem__(self, idx:int) -> None:
        del self._items[idx]

    def sort(self) -> None:
        self._items.sort()

    def shuffle(self) -> None:
        random.shuffle(self._items)

    def push(self, *args) -> None:
        assert all([ isinstance(x, Card) for x in args ]), 'Deck cannot contain non-card items'
        assert all([ x not in self._items for x in args ]), 'Deck already contains such card(s)'
        self._items.extend(args)

    def pop(self) -> Card:
        return self._items.pop()

    def unshift(self, *args) -> None:
        assert all([ isinstance(x, Card) for x in args ]), 'Deck cannot contain non-card items'
        assert all([ x not in self._items for x in args ]), 'Deck already contains such card(s)'
        self._items[0:0] = args

    def shift(self) -> Card:
        return self._items.pop(0)


suits = (
    Suit(code='s', name='spades', order=1, weight=1),
    Suit(code='h', name='hearts', order=2, weight=1),
    Suit(code='d', name='diamonds', order=3, weight=1),
    Suit(code='c', name='clubs', order=4, weight=1),
)
ranks = (
    Rank(code='A', name='Ace', order=1, weight=14),
    Rank(code='2', name='Deuce', order=2, weight=2),
    Rank(code='3', name='Trey', order=3, weight=3),
    Rank(code='4', name='Four', order=4, weight=4),
    Rank(code='5', name='Five', order=5, weight=5),
    Rank(code='6', name='Six', order=6, weight=6),
    Rank(code='7', name='Seven', order=7, weight=7),
    Rank(code='8', name='Eight', order=8, weight=8),
    Rank(code='9', name='Nine', order=9, weight=9),
    Rank(code='T', name='Ten', order=10, weight=10),
    Rank(code='J', name='Jack', order=11, weight=11),
    Rank(code='Q', name='Queen', order=12, weight=12),
    Rank(code='K', name='King', order=13, weight=13),
)
cards = [ Card(rank=r, suit=s) for s in suits for r in ranks ]


class HoldemDeck(Deck):
    """
    Standard Texas hold'em 52-card deck
    """

    def __init__(self) -> None:
        self._items = [ x for x in cards ]

class OmahaDeck(HoldemDeck):
    """
    Standard omaha 52-card deck
    """
    pass
