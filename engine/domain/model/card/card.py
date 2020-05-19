from abc import ABC
from functools import total_ordering


@total_ordering
class Prop(ABC):
    """
    An abstract card property

    Parameters
    ----------
        The same as attributes

    Attributes
    ----------
        code : str
            A code name (single char, read only)
        name : str
            A full name (read only)
        weight : int
            A weight for comparing with other instances (positive, read only)

    Methods
    -------
        __str__()
        __repr__()
        __hash__()
        Comparing operations
    """

    __slots__ = ('_code', '_name', '_weight')

    def __init__(self, code: str, name: str, weight: int) -> None:
        assert len(code) == 1, '{} code must be a single char'.format(self.__class__.__name__)
        assert len(name) > 0, '{} name must not be empty'.format(self.__class__.__name__)
        assert weight > 0, '{} weight must be positive'.format(self.__class__.__name__)

        self._code = code
        self._name = name
        self._weight = weight

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._name)

    def __hash__(self) -> int:
        return hash(self._code)

    def __eq__(self, other: 'Prop') -> bool:
        if self.__class__ != other.__class__:
            raise TypeError(other)
        return self._weight == other._weight

    def __gt__(self, other: 'Prop') -> bool:
        if self.__class__ != other.__class__:
            raise TypeError(other)
        return self._weight > other._weight

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight


class Rank(Prop):
    """
    A card rank (see Prop docs for more information)
    """

    pass


class Suit(Prop):
    """
    A card suit (see Prop docs for more information)
    """

    pass


@total_ordering
class Card:
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

    def __init__(self, rank: Rank, suit: Suit) -> None:
        self._rank = rank
        self._suit = suit

    def __str__(self) -> str:
        return self.code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self.name)

    def __hash__(self) -> int:
        return hash(self.code)

    def __eq__(self, other: 'Card') -> bool:
        return self._rank == other._rank and self._suit == other._suit

    def __gt__(self, other: 'Card') -> bool:
        return (self._rank, self._suit) > (other._rank, other._suit)

    @property
    def rank(self) -> Rank:
        return self._rank

    @property
    def suit(self) -> Suit:
        return self._suit

    @property
    def code(self) -> str:
        return self._rank.code + self._suit.code

    @property
    def name(self) -> str:
        return '{} of {}'.format(self._rank.name, self._suit.name)


__all__ = ('Rank', 'Suit', 'Card')
