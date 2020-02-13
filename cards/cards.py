from typing import List, Optional

from ranks import Rank, standard_ranks
from suits import Suit, standard_suits


class Card():
    """
    Representation of abstract card
    """

    def __init__(self, rank:Rank, suit:Optional[Suit]=None) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        if self.suit:
            return '%s of %s' % (self.rank.__repr__(), self.suit.__repr__(),)
        return self.rank.__repr__()

    def __str__(self) -> str:
        if self.suit:
            return '%s of %s' % (self.rank.__str__(), self.suit.__str__(),)
        return self.rank.__str__()

    def __hash__(self) -> int:
        if self.suit:
            return 256 * ord(self.suit.code) + ord(self.rank.code)
        return ord(self.rank.code)

    def __eq__(self, other:'Card') -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other:'Card') -> bool:
        return self.rank != other.rank or self.suit != other.suit

    def __gt__(self, other:'Card') -> bool:
        return self.rank > other.rank

    def __ge__(self, other:'Card') -> bool:
        return self.rank >= other.rank

    def __lt__(self, other:'Card') -> bool:
        return self.rank < other.rank

    def __le__(self, other:'Card') -> bool:
        return self.rank <= other.rank

    @property
    def code(self) -> str:
        if self.suit:
            return self.rank.code + self.suit.code
        return self.rank.code
    

class CardSet():
    """
    Representation of abstract set of cards
    """

    def __init__(self, items:List[Card]) -> None:
        self.items = set(items)

    def __repr__(self) -> str:
        return repr(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def __eq__(self, other) -> bool:
        return self.items == other.items

    def __ne__(self, other) -> bool:
        return self.items != other.items

    def __contains__(self, item:Card) -> bool:
        return item in self.items

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> iter:
        return iter(self.items)

    def __getitem__(self, key:str) -> Card:
        for x in self.items:
            if x.code == key:
                return x
        raise KeyError('Card %s is not found' % (key,))


standard_cards:CardSet = CardSet([ Card(x, y) for y in standard_suits for x in standard_ranks ])
