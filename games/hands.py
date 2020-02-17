from typing import List, Optional

from cards import Card


class Hand():
    """
    Representation of abstract hand
    """

    _length:int = 0
    _items:set = set()

    def __init__(self, items:Optional[List[Card]]=None):
        if items is not None:
            assert len(items) <= self._length, 'Hand cannot contain more than %d card(s)' % (self._length)
            self._items = set(items)

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

    def __getitem__(self, key:str) -> Card:
        for x in self._items:
            if x.code == key:
                return x
        raise KeyError('Card %s is not found' % (key,))

    @property
    def is_full(self) -> bool:
        return len(self._items) < self._length

    def append(self, item:Card) -> None:
        assert len(self._items) < self._length, 'Hand cannot contain more than %d card(s)' % (self._length,)
        self._items.add(item)


class HoldemHand(Hand):
    """
    Representation of Texas hold'em hand
    """

    _length:int = 2
