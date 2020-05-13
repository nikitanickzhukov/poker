from typing import List, Union
from abc import ABC
import random

from .cards import Card, cards


Idx = Union[int, slice, str, tuple, list]


class Deck(ABC):
    """
    An abstract card deck

    Methods
    -------
        __str__()
        __repr__()
        __bool__()
        __len__()
        __iter__()
        __getitem__()
        __delitem__()
        shuffle()
            Shuffles the deck
        extract():
            Removes and returns a set of cards
    """

    __slots__ = ('_cards',)

    def __init__(self) -> None:
        self._cards = []

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    def __bool__(self) -> bool:
        return bool(self._cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    def __getitem__(self, key: Idx) -> Union[Card, List[Card]]:
        if isinstance(key, (int, slice)):
            return self._cards[key]
        elif isinstance(key, str):
            for card in self._cards:
                if card.code == key:
                    return card
            raise KeyError(key)
        elif isinstance(key, (tuple, list)):
            return [self[x] for x in key]
        raise TypeError(key)

    def __delitem__(self, key: Idx) -> None:
        if isinstance(key, (int, slice)):
            del self._cards[key]
        elif isinstance(key, str):
            for i, card in enumerate(self._cards):
                if card.code == key:
                    del self._cards[i]
                    return
            raise KeyError(key)
        elif isinstance(key, (tuple, list)):
            for x in key:
                del self[x]
        else:
            raise TypeError(key)

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def extract(self, key: Idx) -> Union[Card, List[Card]]:
        value = self[key]
        del self[key]
        return value


class StandardDeck(Deck):
    """
    A standard 52-card deck
    """

    def __init__(self) -> None:
        super().__init__()
        self._cards = list(cards)


__all__ = ('Deck', 'StandardDeck')
