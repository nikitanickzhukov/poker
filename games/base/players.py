from typing import Optional

from .boards import Board
from .pockets import Pocket
from .streets import Street
from .actions import Check


class Player():
    __slots__ = ('pocket', '_nickname', '_chips', '_is_active')

    def __init__(self, nickname:str, chips:int, pocket:Optional[Pocket]=None) -> None:
        self.pocket = pocket
        self._nickname = nickname
        self._chips = chips
        self._is_active = True

    def __repr__(self) -> str:
        if self.pocket is None:
            return '<{}: {}, {} chip(s)'.format(self.__class__.__name__, self._nickname, self._chips)
        return '<{}: {}, {} chip(s), pocket: {}'.format(self.__class__.__name__, self._nickname, self._chips, self.pocket)

    def __str__(self) -> str:
        return self._nickname

    def do_action(self, street:Street, board:Board) -> None:
        return Check()

    def leave_round(self) -> None:
        self._is_active = False

    def lose_chips(self, chips:int) -> None:
        if chips >= self._chips:
            raise ValueError('Player cannot lose more chips than he has')
        self._chips -= chips

    def win_chips(self, chips:int) -> None:
        self._chips += chips

    @property
    def nickname(self):
        return self._nickname

    @property
    def chips(self):
        return self._chips

    @property
    def is_active(self):
        return self._is_active


__all__ = ('Player',)
