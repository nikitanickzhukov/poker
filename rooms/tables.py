from utils.attrs import ListAttr, IntegerAttr
from .gamblers import Gambler
from .boxes import Box


class Table():
    min_boxes = 2
    max_boxes = 10

    boxes = ListAttr(
        type=tuple,
        item_type=Box,
        writable=False,
    )
    empty_boxes = ListAttr(
        type=tuple,
        item_type=Box,
        getter=lambda obj: tuple(x for x in obj.boxes if x.is_empty),
        writable=False,
    )
    active_boxes = ListAttr(
        type=tuple,
        item_type=Box,
        getter=lambda obj: tuple(x for x in obj.boxes if x.is_active),
        writable=False,
    )
    button_idx = IntegerAttr(min_value=0, writable=False)

    def __init__(self) -> None:
        self._boxes = tuple(Box() for _ in range(self.max_boxes))
        self._button_idx = 0

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._boxes)

    def occupy_box(self, box_num:int, gambler:Gambler, chips:int) -> None:
        if any(x.gambler == gambler for x in self._boxes):
            raise ValueError('{!r} is already at the table'.format(gambler))
        self._boxes[box_num].occupy(gambler, chips)

    def leave_box(self, box_num:int) -> None:
        self._boxes[box_num].leave()

    def box_is_empty(self, box_num:int) -> bool:
        return self._boxes[box_num].is_empty


__all__ = ('Table',)
