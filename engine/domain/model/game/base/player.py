from typing import Tuple

from engine.domain.model.card import Card

from .decision import Decision, Check
from .pocket import Pocket


class Player:
    __slots__ = ('_pocket', '_nickname', '_chips', '_state')

    STATE_ACTIVE = 'ACTIVE'
    STATE_FOLDED = 'FOLDED'
    STATE_ALL_IN = 'ALL_IN'

    def __init__(
        self,
        pocket: Pocket,
        nickname: str,
        chips: int,
    ) -> None:
        self._pocket = pocket
        self._nickname = nickname
        self._chips = chips
        self._state = self.STATE_ACTIVE

    def __repr__(self) -> str:
        return '<{}: {}, {} chip(s), {}, {}>'.format(
            self.__class__.__name__,
            self._nickname,
            self._chips,
            self._pocket,
            self._state,
        )

    def __str__(self) -> str:
        if self.is_active():
            return '{}, {} chip(s)'.format(self._nickname, self._chips)
        return '{}, {} chip(s) [{}]'.format(self._nickname, self._chips, self._state)

    def __hash__(self) -> int:
        return hash(self._nickname)

    def post_ante(self, chips: int) -> int:
        return self._post_chips(chips=chips, strict=False)

    def post_blind(self, chips: int) -> int:
        return self._post_chips(chips=chips, strict=False)

    def post_bet(self, chips: int) -> int:
        return self._post_chips(chips=chips, strict=True)

    def do_draw(self) -> Tuple[Card]:
        assert self.is_active(), '{} is not active'.format(self)
        return tuple()

    def do_decision(self) -> Decision:
        assert self.is_active(), '{} is not active'.format(self)
        return Check()

    def _post_chips(self, chips: int, strict: bool) -> int:
        assert self.is_active(), '{} is not active'.format(self)
        assert chips > 0, 'Cannot give negative chips amount'
        if strict:
            assert chips <= self._chips, 'Cannot give more chips than has'
        chips = min(self._chips, chips)
        self._chips -= chips
        if self._chips == 0:
            self.all_in()
        return chips

    def fold(self) -> None:
        assert self.is_active(), '{} is not active'.format(self)
        self._state = self.STATE_FOLDED

    def all_in(self) -> None:
        assert self.is_active(), '{} is not active'.format(self)
        self._state = self.STATE_ALL_IN

    def is_active(self) -> bool:
        return self._state == self.STATE_ACTIVE

    def is_folded(self) -> bool:
        return self._state == self.STATE_FOLDED

    def is_all_in(self) -> bool:
        return self._state == self.STATE_ALL_IN

    @property
    def pocket(self) -> Pocket:
        return self._pocket

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def chips(self) -> int:
        return self._chips


__all__ = ('Player',)
