from abc import ABC

from utils.attrs import ListAttr
from cards import Card


class Street(ABC):
    """
    Representation of abstract street on a board or in a hand
    """

    length = 0
    order = 0

    cards = ListAttr(
        type=set,
        item_type=Card,
        validate=lambda obj, val: len(val) == obj.length,
        writable=False,
    )

    def __init__(self, *cards) -> None:
        items = set(cards)
        self.__class__.cards.validate(self, items)
        self._cards = items

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._cards)

    def __str__(self) -> str:
        return str({ str(x) for x in self._cards })

    def __contains__(self, item:Card) -> bool:
        return item in self._cards

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)


__all__ = ('Street',)
