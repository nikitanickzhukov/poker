from typing import Optional

from .players import Player


class Box():
    def __init__(self, player:Optional[Player]=None, chips:Optional[int]=None) -> None:
        assert (player is None) == (chips is None), 'Player and chips must be both defined or undefined'
        self._player = None
        self._chips = None
        if player:
            self.occupy(player, chips)

    def __repr__(self) -> str:
        if self.is_empty():
            return '<{}: empty>'.format(self.__class__.__name__)
        return '<{}: {!r}, {} chip(s)'.format(self.__class__.__name__, self.player, self.chips)

    def occupy(self, player:Player, chips:int) -> None:
        assert self.is_empty(), 'Box is not empty'
        assert isinstance(player, Player), 'Player must be None or a player instance'
        assert isinstance(chips, int) and chips >= 0, 'Chips must be a positive integer'
        self._player = player
        self._chips = chips

    def leave(self):
        assert not self.is_empty(), 'Box is empty'
        self._player = None
        self._chips = None

    def __get_chips(self) -> int:
        return self._chips

    def __set_chips(self, value:int) -> None:
        assert not self.is_empty(), 'Box is empty'
        assert isinstance(value, int) and value >= 0, 'Chips must be a positive integer'
        self._chips = value

    def is_empty(self) -> bool:
        return self.player is None

    @property
    def player(self) -> Player:
        return self._player

    chips = property(__get_chips, __set_chips)


__all__ = ('Box',)
