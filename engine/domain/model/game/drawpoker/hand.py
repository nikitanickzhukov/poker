from ..base.hand import (
    HandComb, Hand as BaseHand,
    HighCard as BaseHighCard, OnePair as BaseOnePair, TwoPair as BaseTwoPair,
    Trips as BaseTrips, Straight as BaseStraight, Flush as BaseFlush,
    FullHouse as BaseFullHouse, Quads as BaseQuads, StraightFlush as BaseStraightFlush,
    Identifier as BaseIdentifier,
)


class Hand(BaseHand):
    pass


class HighCard(Hand, BaseHighCard):
    pass


class OnePair(Hand, BaseOnePair):
    pass


class TwoPair(Hand, BaseTwoPair):
    pass


class Trips(Hand, BaseTrips):
    pass


class Straight(Hand, BaseStraight):
    pass


class Flush(Hand, BaseFlush):
    pass


class FullHouse(Hand, BaseFullHouse):
    pass


class Quads(Hand, BaseQuads):
    pass


class StraightFlush(Hand, BaseStraightFlush):
    pass


class Identifier(BaseIdentifier):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)


__all__ = (
    'HandComb', 'Hand', 'HighCard', 'OnePair', 'TwoPair', 'Trips',
    'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush', 'Identifier',
)
