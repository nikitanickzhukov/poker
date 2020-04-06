from typing import Union
from abc import ABC
import random

from .cards import Card, cards


class Deck(ABC):
    """
    An abstract card deck

    Parameters
    ----------
        None

    Attributes
    ----------
        None

    Methods
    -------
        __str__()
        __repr__()
        __bool__()
        __contains__()
        __len__()
        __iter__()
        __getitem__()
            Returns a card by index or by code
        __delitem__()
            Deletes a card by index or by code
        shuffle()
            Shuffles the deck
        push(*cards):
            Inserts cards into the tail of the deck
        pop():
            Removes and returns one card from the tail of the deck
        unshift(*cards):
            Inserts cards into the head of the deck
        shift():
            Removes and returns one card from the head of the deck
    """

    def __init__(self) -> None:
        self._items = []

    def __str__(self) -> str:
        return str([ str(x) for x in self._items ])

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, key:Union[slice, int, str]) -> Card:
        if isinstance(key, (slice, int)):
            return self._items[key]
        elif isinstance(key, str):
            for item in self._items:
                if item.code == key:
                    return item
            raise KeyError('Card {} is not found'.format(key))
        else:
            raise AssertionError('Wrong key type')

    def __delitem__(self, key:Union[slice, int, str]) -> None:
        if isinstance(key, (slice, int)):
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

    def push(self, *cards) -> None:
        assert all(isinstance(x, Card) for x in cards), 'Deck must contain `Card` items only'
        assert all(x not in self._items for x in cards), 'Deck already contains such card(s)'
        self._items.extend(cards)

    def pop(self) -> Card:
        return self._items.pop()

    def unshift(self, *cards) -> None:
        assert all(isinstance(x, Card) for x in cards), 'Deck must contain `Card` items only'
        assert all(x not in self._items for x in cards), 'Deck already contains such card(s)'
        self._items[0:0] = cards

    def shift(self) -> Card:
        return self._items.pop(0)


class StandardDeck(Deck):
    """
    A standard 52-card deck
    """

    def __init__(self) -> None:
        super().__init__()
        self._items = list(cards)


__all__ = ('Deck', 'StandardDeck')
