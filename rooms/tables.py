from .gamblers import Gambler
from .boxes import Box


class Table():
    __slots__ = ('_boxes', '_button_idx')
    min_boxes = 2
    max_boxes = 10

    def __init__(self) -> None:
        self._boxes = tuple(Box() for _ in range(self.max_boxes))
        self._button_idx = 0

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def __str__(self) -> str:
        return str([ str(x) for x in self._boxes ])

    def occupy_box(self, box_num:int, gambler:Gambler, chips:int=0) -> None:
        assert all(x.gambler != gambler for x in self._boxes), \
               '{} is already at the table'.format(gambler)
        self._boxes[box_num].occupy(gambler, chips)

    def leave_box(self, box_num:int) -> None:
        self._boxes[box_num].leave()

    def box_is_empty(self, box_num:int) -> bool:
        return self._boxes[box_num].is_empty

    @property
    def boxes(self):
        return self._boxes

    @property
    def empty_boxes(self):
        return tuple(x for x in self._boxes if x.is_empty)

    @property
    def busy_boxes(self):
        return tuple(x for x in self._boxes if not x.is_empty)

    @property
    def button_idx(self):
        return self._button_idx


__all__ = ('Table',)
