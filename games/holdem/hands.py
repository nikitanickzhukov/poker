from ..base import hands


class HoldemMixin():
    pass


class HighCard(HoldemMixin, hands.HighCard):
    pass


class OnePair(HoldemMixin, hands.OnePair):
    pass


class TwoPair(HoldemMixin, hands.TwoPair):
    pass


class Trips(HoldemMixin, hands.Trips):
    pass


class Straight(HoldemMixin, hands.Straight):
    pass

class Flush(HoldemMixin, hands.Flush):
    pass


class FullHouse(HoldemMixin, hands.FullHouse):
    pass


class Quads(HoldemMixin, hands.Quads):
    pass


class StraightFlush(HoldemMixin, hands.StraightFlush):
    pass


class HandIdentifier(HoldemMixin, hands.HandIdentifier):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)


__all__ = ('HandIdentifier', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
