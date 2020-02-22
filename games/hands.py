from abc import ABC

from cards import Card


class Hand(ABC):
    """
    Representation of abstract hand
    """

    _length:int = 0

    def __init__(self, *args) -> None:
        self._items:set = set()
        if args:
            self.append(*args)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __eq__(self, other:'Hand') -> bool:
        return self._items == other._items

    def __ne__(self, other:'Hand') -> bool:
        return self._items != other._items

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    @property
    def is_full(self) -> bool:
        return len(self._items) == self._length

    def append(self, *args) -> None:
        assert all([ isinstance(x, Card) for x in args ]), 'Hand cannot contain non-card items'
        assert len(args) <= self._length - len(self._items), 'Hand cannot contain more than %d card(s)' % (self._length,)
        self._items.update(set(args))


class HoldemHand(Hand):
    """
    Representation of Texas hold'em hand
    """

    _length:int = 2


class OmahaHand(HoldemHand):
    """
    Representation of Omaha hand
    """

    _length:int = 4
