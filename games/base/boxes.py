from typing import Optional

from .players import Player


class Box():
    def __init__(self, player:Optional[Player]=None, stack:Optional[int]=None) -> None:
        assert (player is None) == (stack is None), 'Player and stack must be both defined or undefined'
        self._player = None
        self._stack = None
        if player:
            self.occupy(player, stack)

    def __repr__(self) -> str:
        if self.is_empty():
            return 'Empty box'
        return '{}, {} chip(s)'.format(repr(self.player), self.stack)

    def occupy(self, player:Player, stack:int) -> None:
        assert self.is_empty(), 'Box is not empty'
        assert isinstance(player, Player), 'Player must be None or a player instance'
        assert isinstance(stack, int) and stack >= 0, 'Stack must be a positive integer'
        self._player = player
        self._stack = stack

    def leave(self):
        assert not self.is_empty(), 'Box is empty'
        self._player = None
        self._stack = None

    def win(self, amount:int) -> None:
        assert not self.is_empty(), 'Empty box cannot win'
        assert isinstance(amount, int) and amount >= 0, 'Amount must be a positive integer'
        self._stack += amount

    def lose(self, amount:int) -> None:
        assert not self.is_empty(), 'Empty box cannot lose'
        assert isinstance(amount, int) and amount >= 0, 'Amount must be a positive integer'
        assert amount <= self._stack, 'Box cannot lose more than stack'
        self._stack -= amount

    def is_empty(self) -> bool:
        return self.player is None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def stack(self) -> int:
        return self._stack


__all__ = ('Box',)
