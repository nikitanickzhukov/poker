from utils.attrs import TypedAttr, StringAttr, IntegerAttr, BooleanAttr
from .pockets import Pocket


class Player():
    pocket_class = None
    nickname = StringAttr(
        min_length=1,
        max_length=63,
        writable=False,
    )
    chips = IntegerAttr(min_value=0, writable=False)
    pocket = TypedAttr(type=Pocket, writable=False)
    is_active = BooleanAttr(writable=False)

    def __init__(self, nickname:str, chips:int) -> None:
        self.__class__.nickname.validate(self, nickname)
        self.__class__.chips.validate(self, chips)
        self._nickname = nickname
        self._chips = chips
        self._pocket = self.pocket_class()
        self._is_active = True

    def __repr__(self) -> str:
        return '<{}: {}, {} chip(s), pocket: {}'.format(self.__class__.__name__, self._nickname, self._chips, self._pocket)

    def append(self, *cards) -> None:
        self._pocket.append(*cards)

    def fold(self) -> None:
        self._is_active = False


__all__ = ('Player',)
