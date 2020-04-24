from .gamblers import Gambler


class Box():
    __slots__ = ('_gambler', '_chips', '_is_active')

    def __init__(self) -> None:
        self._gambler = None
        self._chips = None

    def __repr__(self) -> str:
        if self.is_empty:
            return '<{}: empty>'.format(self.__class__.__name__)
        return '<{}: {}, {} chip(s)'.format(self.__class__.__name__, str(self), self._chips)

    def __str__(self) -> str:
        return str(self._gambler)

    def occupy(self, gambler:Gambler, chips:int=0) -> None:
        assert self.is_empty, 'Box is not empty'
        assert chips >= 0, 'Chips must be positive'

        self._gambler = gambler
        self._chips = chips

    def leave(self):
        assert self.is_active, 'Box is not active'
        self._gambler = None
        self._chips = None

    def win_chips(self, chips:int) -> None:
        assert self.is_active, 'Box is not active'
        assert chips >= 0, 'Chips must be positive'
        self._chips += chips

    def lose_chips(self, chips:int) -> None:
        assert self.is_active, 'Box is not active'
        assert chips >= 0, 'Chips must be positive'
        assert chips <= self._chips, 'Box cannot lose more chips than it has'
        self._chips -= chips

    @property
    def gambler(self):
        return self._gambler

    @property
    def chips(self):
        return self._chips

    @property
    def is_empty(self):
        return self._gambler is None

    @property
    def is_active(self):
        return self._gambler is not None


__all__ = ('Box',)
