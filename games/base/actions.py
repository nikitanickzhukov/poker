from abc import ABC

from utils.attrs import IntegerAttr


class Action(ABC):
    with_chips = False

    chips = IntegerAttr(
        min_value=0,
        validate=lambda obj, val: obj.with_chips == (val != 0),
        writable=False,
    )

    def __init__(self, chips:int=0) -> None:
        self.__class__.chips.validate(self, chips)
        self._chips = chips

    def __repr__(self) -> str:
        if self.with_chips:
            return '<{}: {}>'.format(self.__class__.__name__, self._chips)
        return '<{}>'.format(self.__class__.__name__)


class Fold(Action):
    pass


class Check(Action):
    pass


class Call(Action):
    with_chips = True


class Bet(Action):
    with_chips = True


class Raise(Bet):
    pass


class Blind(Bet):
    pass


__all__ = ('Action', 'Fold', 'Check', 'Call', 'Bet', 'Raise', 'Blind')
