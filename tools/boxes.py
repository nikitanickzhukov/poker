from typing import Optional

from .players import Player


class Box():
    def __init__(self) -> None:
        self._player = None
        self._chips = None
        self._is_active = None

    def __repr__(self) -> str:
        if self.is_empty():
            return '<{}: empty>'.format(self.__class__.__name__)
        if not self.is_active():
            return '<{}: {!r}, {} chip(s) [INACTIVE]'.format(self.__class__.__name__, self._player, self._chips)
        return '<{}: {!r}, {} chip(s)'.format(self.__class__.__name__, self._player, self._chips)

    def occupy(self, player:Player, chips:int=0, is_active:bool=True) -> None:
        assert self.is_empty(), 'Box is not empty'
        assert isinstance(player, Player), '`player` must be a `Player` instance'
        assert isinstance(chips, int) and chips >= 0, '`chips` must be a positive integer'
        assert isinstance(is_active, bool), '`is_active` must be a boolean'
        self._player = player
        self._chips = chips
        self._is_active = is_active

    def leave(self):
        assert not self.is_empty(), 'Box is empty'
        self._player = None
        self._chips = None
        self._is_active = None

    def is_empty(self) -> bool:
        return self._player is None

    def __get_chips(self) -> int:
        return self._chips

    def __set_chips(self, value:int) -> None:
        assert not self.is_empty(), 'Box is empty'
        assert isinstance(value, int) and value >= 0, 'Chips must be a positive integer'
        self._chips = value

    @property
    def player(self) -> Optional[Player]:
        return self._player

    @property
    def is_active(self) -> Optional[bool]:
        return self._is_active

    chips = property(__get_chips, __set_chips)


__all__ = ('Box',)
