from ..base import Street


class PreDraw(Street):
    is_pocket = True
    is_hole = True
    length = 5


class Draw(Street):
    with_draw = True


class FirstDraw(Street):
    with_draw = True


class SecondDraw(Street):
    with_draw = True


class ThirdDraw(Street):
    with_draw = True


__all__ = ('PreDraw', 'Draw', 'FirstDraw', 'SecondDraw', 'ThirdDraw')
