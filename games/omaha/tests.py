import unittest

from cards import StandardDeck, cards
from .pockets import Pocket
from .boards import Board
from .hands import Hands, HighCard, OnePair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush


class IdentifyTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_high_card(self):
        # High card in the pocket
        pocket = Pocket(self.deck['As'], self.deck['2s'], self.deck['4d'], self.deck['3c'])
        board = Board(self.deck['Qs'], self.deck['7d'], self.deck['Jh'], self.deck['Kd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['As'])
        self.assertEqual(hand[1], self.deck['Kd'])
        self.assertIn(self.deck['4d'], hand)

        # High card on the board
        pocket = Pocket(self.deck['7s'], self.deck['2s'], self.deck['6c'], self.deck['Tc'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['8s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['Qd'])
        self.assertEqual(hand[1], self.deck['Jh'])
        self.assertIn(self.deck['Tc'], hand)
        self.assertIn(self.deck['7s'], hand)


if __name__ == '__main__':
    unittest.main()
