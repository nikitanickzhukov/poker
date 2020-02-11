from typing import List, Optional

from ranks import Rank, ranks
from suits import Suit, suits


class Card():
    """
    Representation of abstract card

    Tests
    -----
    >>> a = Rank('a', 'rank A', 1)
    >>> b = Rank('b', 'rank B', 2)
    >>> c = Rank('c', 'rank C', 3)
    >>> x = Suit('x', 'suit X')
    >>> y = Suit('y', 'suit Y')
    >>> ax = Card(a, x)
    >>> ay = Card(a, y)
    >>> bx = Card(b, x)
    >>> by = Card(b, y)
    >>> cc = Card(c)
    >>> ax.code
    'ax'
    >>> cc.code
    'c'
    >>> ax == bx
    False
    >>> ax > by
    False
    >>> cc >= ay
    True
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

    Tests
    -----
    >>> a = Rank('a', 'rank A', 1)
    >>> b = Rank('b', 'rank B', 2)
    >>> c = Rank('c', 'rank C', 3)
    >>> x = Suit('x', 'suit X')
    >>> y = Suit('y', 'suit Y')
    >>> ax = Card(a, x)
    >>> ay = Card(a, y)
    >>> bx = Card(b, x)
    >>> by = Card(b, y)
    >>> cc = Card(c)
    >>> s = CardSet([ax, ay, cc,])
    >>> z = s.get('ax')
    >>> z.code
    'ax'
    >>> ax in s
    True
    >>> by in s
    False
    >>> c in s
    True
    """

    items:List[Card] = []

    def __init__(self, items:List[Card]) -> None:
        self.items = items

    def __repr__(self):
        return repr(self.items)

    def __str__(self):
        return str(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def __ne__(self, other):
        return self.items != other.items

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item:Card):
        return item in self.items

    def get(self, code:str) -> Optional[Card]:
        for x in self.items:
            if x.code == code:
                return x
        return None


cards:Card = CardSet([ Card(x, y) for y in suits for x in ranks ])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
