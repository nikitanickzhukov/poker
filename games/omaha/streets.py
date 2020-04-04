from ..base import Street


class Preflop(Street):
    length = 4
    order = 0


class Flop(Street):
    length = 3
    order = 1


class Turn(Street):
    length = 1
    order = 2


class River(Street):
    length = 1
    order = 3


__all__ = ('Preflop', 'Flop', 'Turn', 'River')
