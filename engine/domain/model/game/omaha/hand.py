from typing import Tuple

from engine.domain.model.card import Card
from ..base.hand import (
    HandComb, Hand as BaseHand,
    HighCard as BaseHighCard, OnePair as BaseOnePair, TwoPair as BaseTwoPair,
    Trips as BaseTrips, Straight as BaseStraight, Flush as BaseFlush,
    FullHouse as BaseFullHouse, Quads as BaseQuads, StraightFlush as BaseStraightFlush,
    Identifier as BaseIdentifier,
)


class Hand(BaseHand):
    @classmethod
    def check_comb(cls, comb: HandComb, cards: Tuple[Card]) -> bool:
        pocket_count = 0
        for card in comb.pocket:
            if card in cards:
                pocket_count += 1
                if pocket_count > 2:
                    break
        return pocket_count == 2


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
