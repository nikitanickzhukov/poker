from typing import List, Union
import random

from .cards import Card, CardSet, standard_cards


class Deck():
    """
    Representation of abstract deck
    """

    _items:List[Card] = []

    def __init__(self, items:Union[CardSet, List[Card], None]=None):
        if items is not None:
            self._items = list(items)
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

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, idx:int) -> Card:
        return self._items[idx]

    def __delitem__(self, idx:int) -> None:
        del self._items[idx]

    def shuffle(self) -> None:
        random.shuffle(self._items)

    def push(self, item:Card) -> None:
        self._items.append(item)

    def pop(self) -> Card:
        return self._items.pop()

    def unshift(self, item:Card) -> None:
        self._items.insert(0, item)

    def shift(self) -> Card:
        return self._items.pop(0)


class StandardDeck(Deck):
    """
    Standard 52-card deck
    """

    items:List[Card] = list(standard_cards)
