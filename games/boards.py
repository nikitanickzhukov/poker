from typing import Optional
from abc import ABC

from cards import Card


class Street(ABC):
    """
    Representation of abstract street on a board
    """

    _length:int = 0

    def __init__(self, *args) -> None:
        assert len(args) == self._length, 'Street cannot contain %d card(s) instead of %d' % (len(args), self._length,)
        assert all([ isinstance(x, Street) for x in args ]), 'Street cannot contain non-card items'
        self._items:set = set(args)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __eq__(self, other:'Street') -> bool:
        return self._items == other._items

    def __ne__(self, other:'Street') -> bool:
        return self._items != other._items

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)


class Board(ABC):
    """
    Representation of abstract board
    """

    _streets:tuple = ()

    def __init__(self, *args) -> None:
        self._items:list = []
        if args:
            self.append(*args)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __eq__(self, other:'Board') -> bool:
        return self._items == other._items

    def __ne__(self, other:'Board') -> bool:
        return self._items != other._items

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getattr__(self, key:str) -> Optional[Street]:
        for i in range(len(self._streets)):
            if self._streets[i].__name__.lower() == name:
                return self._items[i] if i < len(self._items) else None
        raise AttributeError

    def append(self, *args) -> None:
        idx = len(self._items)
        for item in args:
            assert idx < len(self._streets), 'Board cannot contain more than %d streets' % (len(self._streets),)
            StreetClass = self._streets[idx]
            assert isinstance(item, StreetClass), 'Street # %d must be a %s instance' % (idx, StreetClass.__name__,)
        self._items.append(*args)


class Flop(Street):
    _length = 3

class Turn(Street):
    _length = 1

class River(Street):
    _length = 1


class HoldemBoard(Board):
    """
    Representation of Texas hold'em board
    """

    _streets:tuple = (Flop, Turn, River,)


class OmahaBoard(HoldemBoard):
    """
    Representation of Omaha board
    """

    pass
