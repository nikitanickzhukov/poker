from .players import Player
from .boxes import Box


class Table():
    min_boxes = 2
    max_boxes = 10

    def __init__(self) -> None:
        self._boxes = [ Box() for _ in range(self.max_boxes) ]

    def __repr__(self) -> str:
        return '<{}: {!r}>'.format(self.__class__.__name__, self._boxes)

    def occupy_box(self, box_num:int, player:Player, chips:int) -> None:
        assert self.box_is_empty(box_num), 'Box {} is not empty'.format(box_num)
        assert all(x.player != player for x in self._boxes), \
               '{!r} is already at the table'.format(player)
        self._boxes[box_num].occupy(player, chips)

    def leave_box(self, box_num:int) -> None:
        assert not self.box_is_empty(box_num), 'Box {} is empty'.format(box_num)
        self._boxes[box_num].leave()

    def box_is_empty(self, box_num:int) -> bool:
        return self._boxes[box_num].is_empty()

    @property
    def boxes(self):
        return self._boxes


__all__ = ('Table',)
