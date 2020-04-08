from functools import total_ordering

from utils.attrs import TypedAttr, StringAttr
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

    rank = TypedAttr(type=Rank, writable=False)
    suit = TypedAttr(type=Suit, writable=False)
    code = StringAttr(getter=lambda obj: obj.rank.code + obj.suit.code, writable=False)
    name = StringAttr(getter=lambda obj: '{} of {}'.format(obj.rank.name, obj.suit.name), writable=False)

    def __init__(self, rank:Rank, suit:Suit) -> None:
        self.__class__.rank.validate(self, rank)
        self.__class__.suit.validate(self, suit)

        self._rank = rank
        self._suit = suit

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self.name)

    def __hash__(self) -> int:
        return hash(self.code)

    def __eq__(self, other:'Card') -> bool:
        return self._rank == other._rank and self._suit == other._suit

    def __gt__(self, other:'Card') -> bool:
        return (self._rank, self.suit) > (other._rank, other._suit)


cards = tuple(Card(rank=r, suit=s) for s in suits for r in ranks)


__all__ = ('Card', 'cards')
