import unittest

from cards import StandardDeck, cards
from .pockets import Pocket
from .boards import Board
from .hands import Hands, HighCard, OnePair, TwoPair, ThreeOfAKind, Straight, Flush, FullHouse, FourOfAKind, StraightFlush


class IdentifyTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_high_card(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), HighCard)

    def test_one_pair(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), OnePair)

    def test_two_pair(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['3h'], self.deck['Qd'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), TwoPair)

    def test_three_of_a_kind(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Ac'], self.deck['Qd'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), ThreeOfAKind)

    def test_straight(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['2d'], self.deck['Jh'], self.deck['4d'], self.deck['5s'])
        self.assertIsInstance(Hands.identify(pocket, board), Straight)

    def test_flush(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Ac'], self.deck['Qs'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), Flush)

    def test_full_house(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Ac'], self.deck['2d'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), FullHouse)

    def test_four_of_a_kind(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Ac'], self.deck['Ah'], self.deck['6s'])
        self.assertIsInstance(Hands.identify(pocket, board), FourOfAKind)

    def test_straight_flush(self):
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4s'], self.deck['Ac'], self.deck['Ah'], self.deck['5s'])
        self.assertIsInstance(Hands.identify(pocket, board), StraightFlush)


if __name__ == '__main__':
    unittest.main()
