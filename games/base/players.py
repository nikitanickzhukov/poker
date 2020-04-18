from typing import Optional

from utils.attrs import TypedAttr, StringAttr, IntegerAttr, BooleanAttr
from .pockets import Pocket


class Player():
    nickname = StringAttr(min_length=1, max_length=63, writable=False)
    chips = IntegerAttr(min_value=0, writable=False)
    pocket = TypedAttr(type=Pocket, nullable=True)
    is_active = BooleanAttr(writable=False)

    def __init__(self, nickname:str, chips:int, pocket:Optional[Pocket]=None) -> None:
        self.__class__.nickname.validate(self, nickname)
        self.__class__.chips.validate(self, chips)
        self.__class__.pocket.validate(self, pocket)
        self._nickname = nickname
        self._chips = chips
        self._pocket = pocket
        self._is_active = True

    def __repr__(self) -> str:
        if self._pocket is None:
            return '<{}: {}, {} chip(s)'.format(self.__class__.__name__, self._nickname, self._chips)
        return '<{}: {}, {} chip(s), pocket: {}'.format(self.__class__.__name__, self._nickname, self._chips, self._pocket)

    def append(self, *cards) -> None:
        assert self._pocket is not None, '`pocket` is not defined'
        self._pocket.append(*cards)

    def deactivate(self) -> None:
        self._is_active = False


__all__ = ('Player',)
