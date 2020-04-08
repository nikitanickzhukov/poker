from typing import Union
from abc import ABC
import random

from utils.attrs import ListAttr
from .cards import Card, cards


class Deck(ABC):
    """
    An abstract card deck

    Parameters
    ----------
        None

    Attributes
    ----------
        cards : list
            A list of cards (read only)

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

    cards = ListAttr(
        type=list,
        item_type=Card,
        validate=lambda obj, val: len(set(val)) == len(val),
        writable=False,
    )

    def __init__(self) -> None:
        self._cards = []

    def __str__(self) -> str:
        return str([ str(x) for x in self._cards ])

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._cards)

    def __bool__(self) -> bool:
        return bool(self._cards)

    def __contains__(self, item:Card) -> bool:
        return item in self._cards

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    def __getitem__(self, key:Union[slice, int, str]) -> Card:
        if isinstance(key, (slice, int)):
            return self._cards[key]
        elif isinstance(key, str):
            for item in self._cards:
                if item.code == key:
                    return item
            raise KeyError('Card {} is not found'.format(key))
        else:
            raise AssertionError('Wrong key type')

    def __delitem__(self, key:Union[slice, int, str]) -> None:
        if isinstance(key, (slice, int)):
            del self._cards[key]
        elif isinstance(key, str):
            ok = False
            for i in range(len(self._cards)):
                if self._cards[i].code == key:
                    del self._cards[i]
                    ok = True
                    break
            if not ok:
                raise KeyError('Card {} is not found'.format(key))
        else:
            raise AssertionError('Wrong key type')

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def push(self, *cards) -> None:
        items = self._cards + list(cards)
        self.__class__.cards.validate(self, items)
        self._cards = items

    def pop(self) -> Card:
        return self._cards.pop()

    def unshift(self, *cards) -> None:
        items = list(cards) + self._cards
        self.__class__.cards.validate(self, items)
        self._cards = items

    def shift(self) -> Card:
        return self._cards.pop(0)


class StandardDeck(Deck):
    """
    A standard 52-card deck
    """

    def __init__(self) -> None:
        items = list(cards)
        self.__class__.cards.validate(self, items)
        super().__init__()
        self._cards = items


__all__ = ('Deck', 'StandardDeck')
