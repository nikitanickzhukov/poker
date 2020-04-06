from functools import total_ordering

from utils.attrs import Attr
from .ranks import Rank, ranks
from .suits import Suit, suits


@total_ordering
class Card():
    """
    A card in a deck

    Parameters
    ----------
        rank : Rank
            A card rank
        suit : Suit
            A card suit

    Attributes
    ----------
        rank : Rank
            A card rank (read only)
        suit : Suit
            A card suit (read only)
        code : str
            A code name (read only)
        name : str
            A full name (read only)

    Methods
    -------
        __str__()
        __repr__()
        __hash__()
        Comparing operations
    """

    rank = Attr()
    suit = Attr()

    def __init__(self, rank:Rank, suit:Suit) -> None:
        assert isinstance(rank, Rank), '`rank` must be a `Rank` instance'
        assert isinstance(suit, Suit), '`suit` must be a `Suit` instance'
        self._rank = rank
        self._suit = suit

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self.name)

    def __hash__(self) -> int:
        return hash(self.code)

    def __eq__(self, other:'Card') -> bool:
        return self.rank == other._rank and self.suit == other._suit

    def __gt__(self, other:'Card') -> bool:
        return (self.rank, self.suit) > (other._rank, other._suit)

    @property
    def code(self) -> str:
        return self.rank.code + self.suit.code

    @property
    def name(self) -> str:
        return '{} of {}'.format(self.rank.name, self.suit.name)


cards = tuple(Card(rank=r, suit=s) for s in suits for r in ranks)


__all__ = ('Card', 'cards')
