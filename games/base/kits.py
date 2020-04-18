from abc import ABC

from utils.attrs import ListAttr
from cards import Card
from .streets import Street


class Kit(ABC):
    """
    Representation of abstract kit (a parent class for boards and hands)
    """

    street_classes = ()

    streets = ListAttr(
        type=list,
        item_type=Street,
        writable=False,
    )
    cards = ListAttr(
        type=tuple,
        item_type=Card,
        getter=lambda obj: tuple(x for s in obj.streets for x in s),
        writable=False,
    )

    def __init__(self, *items) -> None:
        self._streets = []
        if items:
            self.append(*items)

    def __repr__(self) -> str:
        if not self._streets:
            return '<{}: empty>'.format(self.__class__.__name__)
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([ str(x) for x in self.cards ])

    def __contains__(self, item:Card) -> bool:
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
        if len(streets) > len(self.street_classes) - len(self._streets):
            raise ValueError('{} cannot contain more than {} streets'.format(self.__class__, len(self.street_classes)))
        idx = len(self._streets)
        for street in streets:
            StreetClass = self.street_classes[idx]
            if not isinstance(street, StreetClass):
                raise TypeError('Must be a {} instance'.format(StreetClass))
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
        if cards:
            raise ValueError('Extra {} card(s) cannot be added'.format(cards))
        self._append_streets(*streets)


__all__ = ('Kit',)
