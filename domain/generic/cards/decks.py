from abc import ABC
import random

from .cards import Card, cards


class Deck(ABC):
    """
    An abstract card deck

    Parameters
    ----------
        None

    Methods
    -------
        __str__()
        __repr__()
        __bool__()
        __len__()
        __iter__()
        shuffle()
            Shuffles the deck
        pop():
            Removes and returns one card from the tail of the deck
    """

    __slots__ = ('_cards',)

    def __init__(self) -> None:
        self._cards = []

    def __str__(self) -> str:
        return str([ str(x) for x in self._cards ])

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._cards)

    def __bool__(self) -> bool:
        return bool(self._cards)

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()


class StandardDeck(Deck):
    """
    A standard 52-card deck
    """

    def __init__(self) -> None:
        self._cards = list(cards)


__all__ = ('Deck', 'StandardDeck')
