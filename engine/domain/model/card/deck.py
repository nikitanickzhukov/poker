from typing import List, Tuple, Sequence
from abc import ABC
import random

from .card import Card


class Deck(ABC):
    """
    An abstract card deck

    Methods
    -------
        __str__()
        __repr__()
        __bool__()
        __len__()
        shuffle()
            Shuffles the deck
        extract_top_cards():
            Removes and returns a list of cards from the top
        extract_certain_cards():
            Removes and returns a list of certain cards
    """

    __slots__ = ('_cards', '_burnt_cards')
    source = ()

    def __init__(self) -> None:
        self._cards: List[Card] = list(self.source)

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    def __bool__(self) -> bool:
        return bool(self._cards)

    def __len__(self) -> int:
        return len(self._cards)

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def extract_top_cards(self, count: int) -> Tuple[Card]:
        idx = slice(len(self._cards) - count, len(self._cards))
        cards = tuple(self._cards[idx])
        del self._cards[idx]
        return cards

    def extract_certain_cards(self, cards: Sequence[Card]) -> Tuple[Card]:
        i = 0
        while i < len(self._cards):
            if self._cards[i] in cards:
                del self._cards[i]
            else:
                i += 1
        return tuple(cards)


__all__ = ('Deck',)
