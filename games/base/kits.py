from abc import ABC

from cards import Card


class Kit(ABC):
    """
    Representation of abstract kit (a parent class for boards and hands)
    """

    street_classes = ()

    def __init__(self, *args) -> None:
        self._streets = []
        if args:
            self.append(*args)

    def __repr__(self) -> str:
        return repr(self._streets)

    def __str__(self) -> str:
        return str(self._streets)

    def __eq__(self, other:'Kit') -> bool:
        return self.__class__ == other.__class__ and self._streets == other._streets

    def __ne__(self, other:'Kit') -> bool:
        return self.__class__ != other.__class__ or self._streets != other._streets

    def __contains__(self, item:Card) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    @property
    def streets(self) -> list:
        return self._streets

    @property
    def _items(self) -> list:
        return [ x for s in self._streets for x in s ]

    def append(self, *args) -> None:
        if any(isinstance(x, Card) for x in args):
            self._append_cards(*args)
        else:
            self._append_streets(*args)

    def _append_streets(self, *args) -> None:
        assert len(args) <= len(self.street_classes) - len(self._streets), \
               '{} cannot contain more than {} streets'.format(self.__class__.__name__, len(self.street_classes))
        idx = len(self._streets)
        for item in args:
            StreetClass = self.street_classes[idx]
            assert isinstance(item, StreetClass), 'Street {} must be a {} instance'.format(idx, StreetClass.__name__)
            idx += 1
        self._streets.extend(args)

    def _append_cards(self, *args) -> None:
        items = [ x for x in args ]
        streets = []
        street_classes = self.street_classes[len(self._streets):]
        for StreetClass in street_classes:
            assert len(items) >= StreetClass.length, \
                   'Not enough cards to append {}: {} instead of {}'.format(StreetClass.__name__, len(items), StreetClass.length)
            streets.append(StreetClass(*items[0:StreetClass.length]))
            del items[0:StreetClass.length]
            if not items:
                break
        assert len(items) == 0, 'Extra {} card(s) cannot be added'.format(len(items))
        self._append_streets(*streets)
