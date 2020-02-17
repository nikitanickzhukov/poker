from typing import List, Optional

from cards import Card


class Board():
    """
    Representation of abstract 
    """

    _length:int = 0
    _items:List[Card] = []

    def __init__(self, items:Optional[List[Card]]=None):
        if items is not None:
            assert len(items) <= self._length, 'Board cannot contain more than %d card(s)' % (self._length)
            self._items = list(items)

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

    def __getitem__(self, idx:int) -> Card:
        return self._items[idx]

    @property
    def is_full(self) -> bool:
        return len(self._items) < self._length if self._length is not None else False

    def append(self, item:Card) -> None:
        assert len(self._items) < self._length, 'Board cannot contain more than %d card(s)' % (self._length,)
        self._items.append(item)


class HoldemBoard(Board):
    """
    Representation of Texas hold'em board
    """

    _length:int = 5

    @property
    def flop(self):
        return self._items[0:3]

    @property
    def turn(self):
        return self._items[3:4]

    @property
    def river(self):
        return self._items[4:5]
