from ..base import hands


class HighCard(hands.HighCard):
    pass


class OnePair(hands.OnePair):
    pass


class TwoPair(hands.TwoPair):
    pass


class Trips(hands.Trips):
    pass


class Straight(hands.Straight):
    pass


class Flush(hands.Flush):
    pass


class FullHouse(hands.FullHouse):
    pass


class Quads(hands.Quads):
    pass


class StraightFlush(hands.StraightFlush):
    pass


class Identifier(hands.Identifier):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)


__all__ = (
    'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush',
    'FullHouse', 'Quads', 'StraightFlush', 'Identifier',
)
