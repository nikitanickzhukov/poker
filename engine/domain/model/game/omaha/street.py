from ..base import Street


class Preflop(Street):
    is_pocket = True
    is_hole = True
    length = 4


class Flop(Street):
    length = 3


class Turn(Street):
    length = 1


class River(Street):
    length = 1


__all__ = ('Street', 'Preflop', 'Flop', 'Turn', 'River')
