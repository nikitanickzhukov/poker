from typing import Optional

from utils.attrs import TypedAttr, IntegerAttr, BooleanAttr
from .players import Player


class Box():
    player = TypedAttr(
        type=Player,
        nullable=True,
        writable=False
    )
    chips = IntegerAttr(
        min_value=0,
        nullable=True,
        validate=lambda obj, val: (val is None) == obj.is_empty
    )
    is_empty = BooleanAttr(
        getter=lambda obj: obj.player is None,
        writable=False
    )
    is_active = BooleanAttr(
        getter=lambda obj: obj.player is not None,
        writable=False
    )

    def __init__(self) -> None:
        self._player = None
        self._chips = None

    def __repr__(self) -> str:
        if self.is_empty:
            return '<{}: empty>'.format(self.__class__.__name__)
        return '<{}: {!r}, {} chip(s)'.format(self.__class__.__name__, self._player, self._chips)

    def occupy(self, player:Player, chips:int=0) -> None:
        assert self.is_empty, 'Box is not empty'
        self.__class__.player.validate(self, player)
        self._player = player
        self.chips = chips

    def leave(self):
        assert not self.is_empty, 'Box is empty'
        self._player = None
        self._chips = None


__all__ = ('Box',)
