from typing import Tuple
from collections import namedtuple

from engine.domain.model.card import Card
from engine.domain.model.chips import Chips

from .decision import Decision, Check
from .pocket import Pocket


class Player:
    __slots__ = ('_pocket', '_nickname', '_chips', '_state')

    states = namedtuple('state', ('ACTIVE', 'FOLDED', 'ALL_IN'))

    def __init__(
        self,
        pocket: Pocket,
        nickname: str,
        chips: Chips,
    ) -> None:
        self._pocket = pocket
        self._nickname = nickname
        self._chips = chips
        self._state = self.states.ACTIVE

    def __repr__(self) -> str:
        return '<{}: {}, {!r}, {}, {}>'.format(
            self.__class__.__name__,
            self._nickname,
            self._chips,
            self._pocket,
            self._state,
        )

    def __str__(self) -> str:
        return self._nickname

    def __hash__(self) -> int:
        return hash(self._nickname)

    def post_ante(self, chips: Chips) -> Chips:
        return self._post_chips(chips=chips, strict=False)

    def post_blind(self, chips: Chips) -> Chips:
        return self._post_chips(chips=chips, strict=False)

    def post_bet(self, chips: Chips) -> Chips:
        return self._post_chips(chips=chips, strict=True)

    def do_draw(self) -> Tuple[Card]:
        assert self.is_active(), '{} is not active'.format(self)
        return tuple()

    def do_decision(self) -> Decision:
        assert self.is_active(), '{} is not active'.format(self)
        return Check()

    def _post_chips(self, chips: Chips, strict: bool) -> Chips:
        assert self.is_active(), '{} is not active'.format(self)
        if strict:
            assert chips <= self._chips, 'Cannot give more chips than has'
        chips = min(self._chips, chips)
        self._chips -= chips
        if not self._chips:
            self.all_in()
        return chips

    def fold(self) -> None:
        assert self.is_active(), '{} is not active'.format(self)
        self._state = self.states.FOLDED

    def all_in(self) -> None:
        assert self.is_active(), '{} is not active'.format(self)
        self._state = self.states.ALL_IN

    def is_active(self) -> bool:
        return self._state == self.states.ACTIVE

    def is_folded(self) -> bool:
        return self._state == self.states.FOLDED

    def is_all_in(self) -> bool:
        return self._state == self.states.ALL_IN

    @property
    def pocket(self) -> Pocket:
        return self._pocket

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def chips(self) -> Chips:
        return self._chips


__all__ = ('Player',)
