from functools import total_ordering

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

    __slots__ = ('_rank', '_suit')

    def __init__(self, rank:Rank, suit:Suit) -> None:
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
        return (self._rank, self._suit) > (other._rank, other._suit)

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def code(self):
        return self._rank._code + self._suit.code

    @property
    def name(self):
        return '{} of {}'.format(self._rank.name, self._suit.name)


class CardSet(frozenset):
    def __getitem__(self, key:str) -> Card:
        if not hasattr(self, '_mapping'):
            self._mapping = {}
            for card in self:
                self._mapping[card.code] = card
        return self._mapping[key]


cards = tuple(Card(rank=r, suit=s) for s in suits for r in ranks)
cardset = CardSet(cards)


__all__ = ('Card', 'cards', 'cardset')
