from cards import ranks
from kits import Hand as BaseHand, Hands as BaseHands


min_rank = min(ranks)
max_rank = max(ranks)


class Hand(BaseHand):
    @property
    def weight(self):
        return (self.hand_weight, *[ x.rank.weight for x in self._items ])


class HighCard(Hand):
    hand_weight = 1
    first_is_best = True

    def __repr__(self) -> str:
        return 'High card: %s, kickers: %s' % \
               (self._items[0].rank.__repr__(), ', '.join([ x.rank.__repr__() for x in self._items[1:] ]))

    @classmethod
    def identify(cls, comb:list):
        return cls(*comb)


class OnePair(Hand):
    hand_weight = 2
    first_is_best = True

    def __repr__(self) -> str:
        return 'One pair: %ss, kickers: %s' % \
               (self._items[0].rank.__repr__(), ', '.join([ x.rank.__repr__() for x in self._items[2:] ]))

    @classmethod
    def identify(cls, comb:list):
        pair = None
        for i in range(len(comb) - 1):
            if comb[i].rank == comb[i + 1].rank:
                pair = list(comb[i:i + 2])
                break
        if pair:
            kickers = [ x for x in comb if x not in pair ]
            return cls(*(pair + kickers))
        return None


class TwoPair(Hand):
    hand_weight = 3
    first_is_best = True

    def __repr__(self) -> str:
        return 'Two pair: %ss and %ss, kicker: %s' % \
               (self._items[0].rank.__repr__(), self._items[2].rank.__repr__(), self._items[4].rank.__repr__())

    @classmethod
    def identify(cls, comb:list):
        pair1 = None
        pair2 = None
        for i in range(len(comb) - 1):
            if comb[i].rank == comb[i + 1].rank:
                if pair1 is None:
                    pair1 = list(comb[i:i + 2])
                elif pair2 is None:
                    pair2 = list(comb[i:i + 2])
                    break
        if pair1 and pair2:
            pairs = pair1 + pair2
            kickers = [ x for x in comb if x not in pairs ]
            return cls(*(pairs + kickers))
        return None


class Trips(Hand):
    hand_weight = 4
    first_is_best = True

    def __repr__(self) -> str:
        return 'Three of a kind: %ss, kickers: %s' % \
               (self._items[0].rank.__repr__(), ', '.join([ x.rank.__repr__() for x in self._items[3:] ]))

    @classmethod
    def identify(cls, comb:list):
        three = None
        for i in range(len(comb) - 2):
            if comb[i].rank == comb[i + 1].rank == comb[i + 2].rank:
                three = list(comb[i:i + 3])
                break
        if three:
            kickers = [ x for x in comb if x not in three ]
            return cls(*(three + kickers))
        return None


class Straight(Hand):
    hand_weight = 5
    first_is_best = False

    def __repr__(self) -> str:
        return '%s-high straight' % (self._items[0].rank.__repr__(),)

    @classmethod
    def identify(cls, comb:list):
        ok = True
        # Looking for a sequence Xabcd with any X
        for i in range(1, len(comb) - 1):
            if comb[i].rank.weight != comb[i + 1].rank.weight + 1:
                ok = False
                break
        if ok:
            if comb[0].rank.weight == comb[1].rank.weight + 1:
                # Standard straight: 98765 etc.
                return cls(*comb)
            elif comb[0].rank == max_rank and comb[4].rank == min_rank:
                # Wheel straight: 5432A
                return cls(*comb[1:], comb[0])
        return None


class Flush(Hand):
    hand_weight = 6
    first_is_best = True

    def __repr__(self) -> str:
        return '%s-high flush, %s' % \
               (self._items[0].rank.__repr__(), ', '.join([ x.rank.__repr__() for x in self._items[1:] ]))

    @classmethod
    def identify(cls, comb:list):
        ok = True
        for i in range(len(comb) - 1):
            if comb[i].suit != comb[i + 1].suit:
                ok = False
                break
        if ok:
            return cls(*comb)
        return None


class FullHouse(Hand):
    hand_weight = 7
    first_is_best = True

    def __repr__(self) -> str:
        return 'Full house, %ss over %ss' % (self._items[0].rank.__repr__(), self._items[3].rank.__repr__())

    @classmethod
    def identify(cls, comb:list):
        trips = Trips.identify(comb)
        if trips:
            if trips[3].rank == trips[4].rank:
                return cls(*trips)
        return None


class Quads(Hand):
    hand_weight = 8
    first_is_best = True

    def __repr__(self) -> str:
        return 'Four of a kind, %ss, kicker: %s' % (self._items[0].rank.__repr__(), self._items[4].rank.__repr__())

    @classmethod
    def identify(cls, comb:list):
        trips = Trips.identify(comb)
        if trips:
            if trips[3].rank == trips[0].rank:
                return cls(*trips)
            elif trips[4].rank == trips[0].rank:
                return cls(*trips[0:3], trips[4], trips[3])
        return None


class StraightFlush(Hand):
    hand_weight = 9
    first_is_best = False

    def __repr__(self) -> str:
        if self._items[0].rank == max_rank:
            return 'Royal flush'
        return '%s-high straight flush' % (self._items[0].rank.__repr__(),)

    @classmethod
    def identify(cls, comb:list):
        if Flush.identify(comb):
            straight = Straight.identify(comb)
            if straight:
                return cls(*straight)
        return None


class Hands(BaseHands):
    length = 5
    hand_classes = (StraightFlush, Quads, FullHouse, Flush, Straight, Trips, TwoPair, OnePair, HighCard)


__all__ = ('Hands', 'HighCard', 'OnePair', 'TwoPair', 'Trips', 'Straight', 'Flush', 'FullHouse', 'Quads', 'StraightFlush')
