from abc import ABC
from typing import Sequence, Tuple, Union

from domain.cards import Card


class Street(ABC):
    """
    Representation of abstract street on a board or in a hand
    """

    __slots__ = ('_cards',)
    length = 0
    is_pocket = False

    def __init__(self, cards: Sequence[Card]) -> None:
        assert len(cards) == self.length, 'Must contain {} card(s)'.format(self.length)
        self._cards = set(cards)

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    def __contains__(self, item: Union[Card, str]) -> bool:
        if isinstance(item, Card):
            return item in self._cards
        elif isinstance(item, str):
            return item in [x.code for x in self._cards]
        raise TypeError(item)

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    @property
    def cards(self) -> Tuple[Card]:
        return tuple(self._cards)


__all__ = ('Street',)
