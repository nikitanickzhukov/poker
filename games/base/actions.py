from abc import ABC


class Action(ABC):
    __slots__ = ('_chips',)
    with_chips = False

    def __init__(self, chips:int=0) -> None:
        assert chips >= 0 and self.with_chips == (chips > 0), \
            '{} cannot contain {} chip(s)'.format(self.__class__.__name__, chips)

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
