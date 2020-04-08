from abc import ABC

from utils.attrs import IntegerAttr


class Action(ABC):
    is_aggressive = False
    with_amount = False

    amount = IntegerAttr(
        min_value=0,
        validate=lambda obj, val: obj.with_amount == (val != 0),
        writable=False,
    )

    def __init__(self, amount:int=0) -> None:
        self.__class__.amount.validate(self, amount)
        self._amount = amount

    def __repr__(self) -> str:
        if self.with_amount:
            return '<{}: {}>'.format(self.__class__.__name__, self._amount)
        return '<{}>'.format(self.__class__.__name__)


class Fold(Action):
    pass


class Check(Action):
    pass


class Call(Action):
    with_amount = True


class Bet(Action):
    is_aggressive = True
    with_amount = True


class Raise(Action):
    is_aggressive = True
    with_amount = True


__all__ = ('Action', 'Fold', 'Check', 'Call', 'Bet', 'Raise')
