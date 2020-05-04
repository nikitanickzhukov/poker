from abc import ABC

from domain.generic.cards import Card

from .streets import Street


class Kit(ABC):
    """
    Representation of abstract kit (a parent class for boards and hands)
    """

    __slots__ = ('_streets',)
    street_classes = ()

    def __init__(self, *items) -> None:
        self._streets = []
        if items:
            self.append(*items)

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

    def append(self, *items) -> None:
        if any(isinstance(x, Card) for x in items):
            self._append_cards(*items)
        else:
            self._append_streets(*items)

    def _append_streets(self, *streets) -> None:
        assert len(streets) <= len(self.street_classes) - len(self._streets), \
            '{} cannot contain more than {} streets'.format(self.__class__, len(self.street_classes))

        idx = len(self._streets)
        for street in streets:
            street_class = self.street_classes[idx]
            assert isinstance(street, street_class), 'Must be a {} instance'.format(street_class)
            idx += 1
        self._streets.extend(streets)

    def _append_cards(self, *cards) -> None:
        cards = list(cards)
        streets = []
        street_classes = self.street_classes[len(self._streets):]
        for StreetClass in street_classes:
            streets.append(StreetClass(*cards[0:StreetClass.length]))
            del cards[0:StreetClass.length]
            if not cards:
                break
        assert len(cards) == 0, 'Extra {} card(s) cannot be added'.format(cards)
        self._append_streets(*streets)

    @property
    def streets(self) -> tuple:
        return tuple(self._streets)

    @property
    def cards(self) -> tuple:
        return tuple(x for s in self._streets for x in s)


__all__ = ('Kit',)
