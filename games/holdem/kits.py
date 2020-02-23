from itertools import combinations

from kits import Street as BaseStreet, Pocket as BasePocket, Boards as BaseBoard, Hand as BaseHand


class Preflop(BaseStreet):
    length = 2

class Flop(BaseStreet):
    length = 3

class Turn(BaseStreet):
    length = 1

class River(BaseStreet):
    length = 1


class Pocket(BasePocket):
    street_classes = (Preflop,)

class Board(BaseBoard):
    street_classes = (Flop, Turn, River,)


class Hand(BaseHand):
    length = 5

    @classmethod
    def identify(cls, pocket:Pocket, board:Board):
        cards = cls.get_cards(pocket, board)
        combs = cls.get_combs(cards)
        for comb in combs:
            hand = cls.detect(comb)
            if hand:
                return hand
        return None

    @classmethod
    def detect(self, comb:tuple):
        return None

    @classmethod
    def get_cards(cls, pocket:Pocket, board:Board) -> list:
        return [ x for x in pocket ] + [ y for y in board ]

    @classmethod
    def get_combs(cls, cards:list) -> iter:
        return combinations(cards, cls.length)


class HighCard(Hand):
    weight = 1

class OnePair(Hand):
    weight = 2

class TwoPair(Hand):
    weight = 3

class ThreeOfAKind(Hand):
    weight = 4

class Straight(Hand):
    weight = 5

class Flush(Hand):
    weight = 6

class FullHouse(Hand):
    weight = 7

class FourOfAKind(Hand):
    weight = 8

class StraightFlush(Hand):
    weight = 9
