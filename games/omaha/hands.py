from ..base import hands


class OmahaMixin():
    @classmethod
    def check_comb(cls, hand:hands.HandComb, comb:tuple) -> bool:
        pocket_count = 0
        for card in hand.pocket:
            if card in comb:
                pocket_count += 1
                if pocket_count > 2:
                    break
        return pocket_count == 2


class HighCard(OmahaMixin, hands.HighCard):
    pass


class OnePair(OmahaMixin, hands.OnePair):
    pass


class TwoPair(OmahaMixin, hands.TwoPair):
    pass


class Trips(OmahaMixin, hands.Trips):
    pass


class Straight(OmahaMixin, hands.Straight):
    pass

class Flush(OmahaMixin, hands.Flush):
    pass


class FullHouse(OmahaMixin, hands.FullHouse):
    pass


class Quads(OmahaMixin, hands.Quads):
    pass


class StraightFlush(OmahaMixin, hands.StraightFlush):
    pass


class HandIdentifier(hands.HandIdentifier):
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)


__all__ = ('HandIdentifier', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
