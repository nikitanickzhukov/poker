from typing import Optional, Sequence
from abc import ABC

from domain.generic.cards import Card

from .streets import Street


class Kit(ABC):
    """
    Representation of abstract kit (a parent class for board and pocket)
    """

    __slots__ = ('_streets',)

    def __init__(self, streets: Optional[Sequence[Street]] = None) -> None:
        self._streets = streets or []

    def __repr__(self) -> str:
        if not self._streets:
            return '<{}: empty>'.format(self.__class__.__name__)
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self.cards])

    def __contains__(self, item: Card) -> bool:
        return item in self.cards

    def __len__(self) -> int:
        return len(self.cards)

    def __iter__(self) -> iter:
        return iter(self.cards)

    def append(self, street: Street) -> None:
        self._streets.append(street)

    @property
    def streets(self) -> Sequence[Street]:
        return tuple(self._streets)

    @property
    def cards(self) -> Sequence[Card]:
        return tuple(x for s in self._streets for x in s)


__all__ = ('Kit',)
