from typing import List, Optional

from .ranks import Rank
from .suits import Suit


class Card():
    """
    Representation of abstract card

    Tests
    -----
    >>> a = Rank('a', 'rank A', 1)
    >>> b = Rank('b', 'rank B', 2)
    >>> x = Suit('x', 'suit X')
    >>> y = Suit('y', 'suit Y')
    >>> ax = Card(a, z)
    >>> ay = Card(a, y)
    >>> bx = Card(b, x)
    >>> by = Card(b, y)
    >>> ax
    rank A of suit X
    """

    def __init__(self, rank:Rank, suit:Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return '%s of %s' % (self.rank.__repr__(), self.suit.__repr__(),)

    def __str__(self) -> str:
        return '%s of %s' % (self.rank.__str__(), self.suit.__str__(),)

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
