from .actions import Action, Fold, Check, Bet, Raise, Blind, Ante
from .streets import Street
from .boards import Board
from .pockets import Pocket


class Player:
    __slots__ = ('_pocket', '_nickname', '_chips', '_is_active')

    def __init__(
        self,
        pocket: Pocket,
        nickname: str,
        chips: int,
        is_active: bool = True,
    ) -> None:
        self._pocket = pocket
        self._nickname = nickname
        self._chips = chips
        self._is_active = is_active

    def __repr__(self) -> str:
        return '<{}: {}, {} chip(s), {}'.format(
            self.__class__.__name__,
            self._nickname,
            self._chips,
            self._pocket,
        )

    def __str__(self) -> str:
        return self._nickname

    def post_ante(self, chips: int) -> Ante:
        if chips > self._chips:
            chips = self._chips
        self._chips -= chips
        return Ante(chips=chips)

    def post_blind(self, chips: int) -> Blind:
        if chips > self._chips:
            chips = self._chips
        self._chips -= chips
        return Blind(chips=chips)

    def do_action(self, board: Board, street: Street) -> Action:
        assert self.is_active, '{} is not active'.format(self.__class__.__name__)
        return Check()

    def leave_round(self) -> None:
        self._is_active = False

    def win_chips(self, chips: int) -> None:
        assert self.is_active, '{} is not active'.format(self.__class__.__name__)
        assert chips > 0, '{} cannot win negative chips'.format(self.__class__.__name__)
        self._chips += chips

    @property
    def pocket(self):
        return self._pocket

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
