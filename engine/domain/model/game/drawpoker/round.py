from ..base import Round
from .street import PreDraw, Draw, FirstDraw, SecondDraw, ThirdDraw
from .hand import Identifier


class DrawPokerRound(Round):
    street_classes = (PreDraw, Draw)
    identifier_class = Identifier


class TripleDrawPokerRound(DrawPokerRound):
    street_classes = (PreDraw, FirstDraw, SecondDraw, ThirdDraw)


__all__ = ('DrawPokerRound', 'TripleDrawPokerRound')
