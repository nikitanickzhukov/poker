from abc import ABC

from domain.generic.cards import Card


class Street(ABC):
    """
    Representation of abstract street on a board or in a hand
    """

    __slots__ = ('_cards',)
    length = 0
    order = 0

    def __init__(self, *cards) -> None:
        assert len(cards) == self.length, \
            '{} cannot contain {} card(s)'.format(self.__class__.__name__, len(cards))
        self._cards = set(cards)

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([str(x) for x in self._cards])

    def __contains__(self, item: Card) -> bool:
        return item in self._cards

    def __len__(self) -> int:
        return len(self._cards)

    def __iter__(self) -> iter:
        return iter(self._cards)

    @property
    def cards(self):
        return self._cards


__all__ = ('Street',)
