from typing import Optional

from utils.attrs import TypedAttr, StringAttr, IntegerAttr, BooleanAttr
from .boards import Board
from .pockets import Pocket
from .streets import Street
from .actions import Check


class Player():
    nickname = StringAttr(min_length=1, max_length=63, writable=False)
    chips = IntegerAttr(min_value=0, writable=False)
    pocket = TypedAttr(type=Pocket, nullable=True)
    is_active = BooleanAttr(writable=False)

    def __init__(self, nickname:str, chips:int, pocket:Optional[Pocket]=None) -> None:
        self.__class__.nickname.validate(self, nickname)
        self.__class__.chips.validate(self, chips)
        self.__class__.pocket.validate(self, pocket)
        self._nickname = nickname
        self._chips = chips
        self._pocket = pocket
        self._is_active = True

    def __repr__(self) -> str:
        if self._pocket is None:
            return '<{}: {}, {} chip(s)'.format(self.__class__.__name__, self._nickname, self._chips)
        return '<{}: {}, {} chip(s), pocket: {}'.format(self.__class__.__name__, self._nickname, self._chips, self._pocket)

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


__all__ = ('Player',)
