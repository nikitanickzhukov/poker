from typing import Sequence, Type

from .street import Street


class State:
    __slots__ = ('_street_classes', '_street_class', '_stage', '_player')

    def __init__(self, street_classes: Sequence[Type[Street]]) -> None:
        self._street_classes = street_classes
        self._street_class = street_classes[0]


__all__ = ('State',)
