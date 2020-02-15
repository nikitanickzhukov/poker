from typing import List, Union
import random

from cards import Card, CardSet, standard_cards


class Deck():
    """
    Representation of abstract deck
    """

    items:List[Card] = []

    def __init__(self, items:Union[CardSet, List[Card], None]=None):
        if items is not None:
            self.items = list(items)

    def __repr__(self) -> str:
        return repr(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def __eq__(self, other:'Deck') -> bool:
        return self.items == other.items

    def __ne__(self, other:'Deck') -> bool:
        return self.items != other.items

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> iter:
        return iter(self.items)

    def __getitem__(self, idx:int) -> Card:
        return self.items[idx]

    def __delitem__(self, idx:int) -> None:
        del self.items[idx]

    def shuffle(self) -> None:
        random.shuffle(self.items)

    def push(self, item:Card) -> None:
        self.items.append(item)

    def pop(self) -> Card:
        return self.items.pop()

    def unshift(self, item:Card) -> None:
        self.items.insert(0, item)

    def shift(self) -> Card:
        return self.items.pop(0)


class StandardDeck(Deck):
    """
    Standard 52-card deck
    """

    items:List[Card] = list(standard_cards)
