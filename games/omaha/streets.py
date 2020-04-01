from ..base import Street


class Preflop(Street):
    length = 4

class Flop(Street):
    length = 3

class Turn(Street):
    length = 1

class River(Street):
    length = 1


__all__ = ('Preflop', 'Flop', 'Turn', 'River')
