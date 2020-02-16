from typing import List, Optional

from .ranks import Rank, standard_ranks
from .suits import Suit, standard_suits


class Card():
    """
    Representation of abstract card
    """

    def __init__(self, rank:Rank, suit:Suit) -> None:
        self._rank = rank
        self._suit = suit

    def __repr__(self) -> str:
        return '%s of %s' % (self._rank.__repr__(), self._suit.__repr__(),)

    def __str__(self) -> str:
        return '%s of %s' % (self._rank.__str__(), self._suit.__str__(),)

    def __hash__(self) -> int:
        return 256 * ord(self._suit.code) + ord(self._rank.code)

    def __eq__(self, other:'Card') -> bool:
        return self._rank == other._rank and self._suit == other._suit

    def __ne__(self, other:'Card') -> bool:
        return self._rank != other._rank or self._suit != other._suit

    def __gt__(self, other:'Card') -> bool:
        return self._rank > other._rank

    def __ge__(self, other:'Card') -> bool:
        return self._rank >= other._rank

    def __lt__(self, other:'Card') -> bool:
        return self._rank < other._rank

    def __le__(self, other:'Card') -> bool:
        return self._rank <= other._rank

    @property
    def rank(self) -> str:
        return self._rank

    @property
    def suit(self) -> str:
        return self._suit

    @property
    def code(self) -> str:
        return self._rank.code + self._suit.code


class CardSet():
    """
    Representation of abstract set of cards
    """

    def __init__(self, items:List[Card]) -> None:
        self._items = set(items)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __eq__(self, other) -> bool:
        return self._items == other._items

    def __ne__(self, other) -> bool:
        return self._items != other._items

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, key:str) -> Card:
        for x in self._items:
            if x.code == key:
                return x
        raise KeyError('Card %s is not found' % (key,))


standard_cards:CardSet = CardSet([ Card(x, y) for y in standard_suits for x in standard_ranks ])
