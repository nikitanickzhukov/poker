from abc import ABC

from cards import Card


class Street(ABC):
    """
    Representation of abstract street on a board or in a hand
    """

    _length = 0

    def __init__(self, *args) -> None:
        assert len(args) == self._length, 'Street cannot contain %d card(s) instead of %d' % (len(args), self._length,)
        assert all([ isinstance(x, Card) for x in args ]), 'Street cannot contain non-card items'
        self._items = set(args)

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



class Kit(ABC):
    """
    Representation of abstract list of streets (a parent class for boards and hands)
    """

    _street_classes = ()

    def __init__(self, *args) -> None:
        self._streets = []
        if args:
            self.append(*args)

    def __repr__(self) -> str:
        return repr(self._streets)

    def __str__(self) -> str:
        return str(self._streets)

    def __eq__(self, other:'Kit') -> bool:
        return self._streets == other._streets

    def __ne__(self, other:'Kit') -> bool:
        return self._streets != other._streets

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    @property
    def street_classes(self) -> list:
        return self._street_classes

    @property
    def street_names(self) -> list:
        return [ x.__name__.lower() for x in self._street_classes ]

    @property
    def streets(self) -> list:
        return self._streets

    @property
    def _items(self) -> list:
        return [ x for s in self._streets for x in s ]

    def append(self, *args) -> None:
        idx = len(self._streets)
        for item in args:
            assert idx < len(self._street_classes), '%s cannot contain more than %d streets' % (self.__class__.__name__, len(self._street_classes),)
            StreetClass = self._street_classes[idx]
            assert isinstance(item, StreetClass), 'Street %d must be a %s instance' % (idx, StreetClass.__name__,)
            idx += 1
        self._streets.extend(args)


class HoldemPreflop(Street):
    _length = 2

class OmahaPreflop(HoldemPreflop):
    _length = 4

class Flop(Street):
    _length = 3

class Turn(Street):
    _length = 1

class River(Street):
    _length = 1


class HoldemBoard(Kit):
    _street_classes = (Flop, Turn, River,)

class HoldemHand(Kit):
    _street_classes = (HoldemPreflop,)


class OmahaBoard(HoldemBoard):
    pass

class OmahaHand(HoldemHand):
    _street_classes = (OmahaPreflop,)
