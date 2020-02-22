from abc import ABC

from cards import Card


class Kit(ABC):
    """
    Representation of abstract kit (a parent class for boards and hands)
    """

    _street_classes = ()

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
    def street_classes(self) -> list:
        return self._street_classes

    @property
    def street_names(self) -> list:
        return [ x.__name__.lower() for x in self._street_classes ]

    @property
    def streets(self) -> list:
        return self._streets

    @property
    def _items(self) -> list:
        return [ x for s in self._streets for x in s ]

    def append(self, *args) -> None:
        idx = len(self._streets)
        for item in args:
            assert idx < len(self._street_classes), '%s cannot contain more than %d streets' % (self.__class__.__name__, len(self._street_classes),)
            StreetClass = self._street_classes[idx]
            assert isinstance(item, StreetClass), 'Street %d must be a %s instance' % (idx, StreetClass.__name__,)
            idx += 1
        self._streets.extend(args)
