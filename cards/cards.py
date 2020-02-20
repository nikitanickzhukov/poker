from .ranks import Rank
from .suits import Suit


class Card():
    """
    Representation of abstract card
    """

    def __init__(self, rank:Rank, suit:Suit) -> None:
        assert isinstance(rank, Rank), 'Rank cannot be non-rank instance'
        assert isinstance(suit, Suit), 'Suit cannot be non-suit instance'
        self._rank = rank
        self._suit = suit

    def __repr__(self) -> str:
        return '%s of %s' % (self.rank.__repr__(), self.suit.__repr__(),)

    def __str__(self) -> str:
        return '%s of %s' % (self.rank.__str__(), self.suit.__str__(),)

    def __hash__(self) -> int:
        return 256 * ord(self.suit.code) + ord(self.rank.code)

    def __eq__(self, other:'Card') -> bool:
        return self.rank == other._rank and self.suit == other._suit

    def __ne__(self, other:'Card') -> bool:
        return self.rank != other._rank or self.suit != other._suit

    def __gt__(self, other:'Card') -> bool:
        return (self.rank, self.suit,) > (other._rank, other._suit,)

    def __ge__(self, other:'Card') -> bool:
        return (self.rank, self.suit,) >= (other._rank, other._suit,)

    def __lt__(self, other:'Card') -> bool:
        return (self.rank, self.suit,) < (other._rank, other._suit,)

    def __le__(self, other:'Card') -> bool:
        return (self.rank, self.suit,) <= (other._rank, other._suit,)

    @property
    def rank(self) -> str:
        return self._rank

    @property
    def suit(self) -> str:
        return self._suit

    @property
    def code(self) -> str:
        return self.rank.code + self.suit.code
