from abc import ABC


class Action(ABC):
    is_aggressive = False
    with_amount = False

    def __init__(self, amount:int=0) -> None:
        assert isinstance(amount, int), 'Amount must be an integer'
        if self.with_amount:
            assert amount > 0, 'Amount is required for {}'.format(self.__class__.__name__)
        else:
            assert amount == 0, 'Amount must be zero for {}'.format(self.__class__.__name__)
        self._amount = amount

    @property
    def amount(self):
        return self._amount


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
