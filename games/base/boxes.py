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
        return '<{}: {}, {} chip(s)'.format(self.__class__.__name__, repr(self.player), self.chips)

    def occupy(self, player:Player, chips:int) -> None:
        assert self.is_empty(), 'Box is not empty'
        assert isinstance(player, Player), 'Player must be None or a player instance'
        assert isinstance(chips, int) and chips >= 0, 'Stack must be a positive integer'
        self._player = player
        self._chips = chips

    def leave(self):
        assert not self.is_empty(), 'Box is empty'
        self._player = None
        self._chips = None

    def win(self, amount:int) -> None:
        assert not self.is_empty(), 'Empty box cannot win'
        assert isinstance(amount, int) and amount >= 0, 'Amount must be a positive integer'
        self._chips += amount

    def lose(self, amount:int) -> None:
        assert not self.is_empty(), 'Empty box cannot lose'
        assert isinstance(amount, int) and amount >= 0, 'Amount must be a positive integer'
        assert amount <= self._chips, 'Box cannot lose more than chips'
        self._chips -= amount

    def is_empty(self) -> bool:
        return self.player is None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def chips(self) -> int:
        return self._chips


__all__ = ('Box',)
