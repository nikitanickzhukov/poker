from kits import Street as BaseStreet


class Preflop(BaseStreet):
    length = 2

class Flop(BaseStreet):
    length = 3

class Turn(BaseStreet):
    length = 1

class River(BaseStreet):
    length = 1


__all__ = ('Preflop', 'Flop', 'Turn', 'River')
