from abc import ABC

from cards import Card


class Street(ABC):
    """
    Representation of abstract street on a board or in a hand
    """

    length = 0

    def __init__(self, *args) -> None:
        assert len(args) == self.length, 'Street cannot contain %d card(s) instead of %d' % (len(args), self.length,)
        assert all([ isinstance(x, Card) for x in args ]), 'Street cannot contain non-card items'
        self._items = set(args)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __eq__(self, other:'Street') -> bool:
        return self.__class__ == other.__class__ and self._items == other._items

    def __ne__(self, other:'Street') -> bool:
        return self.__class__ != other.__class__ or self._items != other._items

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)


class HoldemPreflop(Street):
    length = 2

class OmahaPreflop(Street):
    length = 4

class Flop(Street):
    length = 3

class Turn(Street):
    length = 1

class River(Street):
    length = 1
