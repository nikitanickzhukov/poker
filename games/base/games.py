from typing import List, Optional
from abc import ABC

from cards import Deck
from .rounds import Round
from .players import Player
from .pockets import Pocket
from .board import Board
from .boxes import Box


class Game(ABC):
    min_players = 2
    max_players = 10
    round_class = None
    pocket_class = None
    board_class = None
    deck_class = None

    def __init__(self, bb:int, sb:int, ante:int=0) -> None:
        assert issubclass(self.round_class, Round), 'Round class must be a round subclass'
        assert issubclass(self.pocket_class, Pocket), 'Pocket class must be a pocket subclass'
        assert issubclass(self.board_class, Board), 'Board class must be a board subclass'
        assert issubclass(self.deck_class, Deck), 'Deck class must be a deck subclass'

        assert isinstance(bb, int) and bb > 0, 'BB must be a positive integer'
        assert isinstance(sb, int) and 0 < sb <= bb, 'SB must be a positive integer less or equal to BB'
        assert isinstance(ante, int) and ante >= 0, 'Ante must be a zero or a positive integer'

        self._bb = bb
        self._sb = sb
        self._ante = ante
        self._boxes = [ Box() for _ in range(max_players) ]

    def occupy_box(self, player:Player, stack:int, box_num:int) -> None:
        assert self.box_is_empty(box_num), 'Box {} is not empty'.format(box_num)
        self._boxes[box_num].occupy(player, stack)

    def leave_box(self, box_num:int) -> None:
        assert not self.box_is_empty(box_num), 'Box {} is empty'.format(box_num)
        self._boxes[box_num].leave()

    def box_is_empty(self, box:int) -> bool:
        return self._boxes[box].is_empty()

    @property
    def bb(self) -> int:
        return self._bb

    @property
    def sb(self) -> int:
        return self._sb

    @property
    def ante(self) -> int:
        return self._ante

    @property
    def boxes(self):
        return self._boxes


__all__ = ('Game',)
