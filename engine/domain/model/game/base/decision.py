from abc import ABC
from typing import Optional

from engine.domain.model.chips import Chips


class Decision(ABC):
    __slots__ = ('_player', '_chips')
    with_chips = False
    is_aggressive = False

    def __init__(self, chips: Optional[Chips] = None) -> None:
        if chips is None:
            chips = Chips(amount=0)
        assert self.with_chips == bool(chips), \
            '{} cannot contain {}'.format(self.__class__.__name__, chips)
        self._chips = chips

    def __repr__(self) -> str:
        if self.with_chips:
            return '<{}: {!r}>'.format(self.__class__.__name__, self._chips)
        return '<{}>'.format(self.__class__.__name__)

    def __str__(self) -> str:
        if self.with_chips:
            return '{} {}'.format(self.__class__.__name__, self._chips)
        return self.__class__.__name__

    @property
    def chips(self):
        return self._chips


class Fold(Decision):
    pass


class Check(Decision):
    pass


class Call(Decision):
    with_chips = True


class Bet(Decision):
    with_chips = True
    is_aggressive = False


class Raise(Bet):
    pass


__all__ = ('Decision', 'Fold', 'Check', 'Call', 'Bet', 'Raise')
