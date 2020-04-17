from typing import Optional

from utils.attrs import TypedAttr, IntegerAttr, BooleanAttr
from .gamblers import Gambler


class Box():
    gambler = TypedAttr(
        type=Gambler,
        nullable=True,
        writable=False
    )
    chips = IntegerAttr(
        min_value=0,
        nullable=True,
        validate=lambda obj, val: (val is None) == obj.is_empty
    )
    is_empty = BooleanAttr(
        getter=lambda obj: obj.gambler is None,
        writable=False
    )
    is_active = BooleanAttr(
        getter=lambda obj: obj.gambler is not None,
        writable=False
    )

    def __init__(self) -> None:
        self._gambler = None
        self._chips = None

    def __repr__(self) -> str:
        if self.is_empty:
            return '<{}: empty>'.format(self.__class__.__name__)
        return '<{}: {!r}, {} chip(s)'.format(self.__class__.__name__, self._gambler, self._chips)

    def occupy(self, gambler:Gambler, chips:int=0) -> None:
        assert self.is_empty, 'Box is not empty'
        self.__class__.gambler.validate(self, gambler)
        self._gambler = gambler
        self.chips = chips

    def leave(self):
        assert not self.is_empty, 'Box is empty'
        self._gambler = None
        self._chips = None


__all__ = ('Box',)
