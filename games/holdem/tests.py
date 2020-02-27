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
        # High card in the pocket
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['As'])
        self.assertEqual(hand[1], self.deck['Qd'])

        # High card on the board
        pocket = Pocket(self.deck['7s'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['Qd'])
        self.assertEqual(hand[1], self.deck['Jh'])

    def test_one_pair(self):
        # One pair, in the pocket and on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'], ]))
        self.assertEqual(hand[2], self.deck['Qd'])

        # One pair, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['4s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['4d'], self.deck['4s'], ]))
        self.assertEqual(hand[2], self.deck['As'])

        # One pair, in the pocket only
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'], ]))
        self.assertEqual(hand[2], self.deck['Qd'])

    def test_two_pair(self):
        # Two pair, in the pocket and on the board (mixed)
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['2h'], self.deck['Qd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'], ]))
        self.assertEqual(set(hand[2:4]), set([ self.deck['2s'], self.deck['2h'], ]))
        self.assertEqual(hand[4], self.deck['Qd'])

        # Two pair, in the pocket and on the board (separetely)
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['3d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'], ]))
        self.assertEqual(set(hand[2:4]), set([ self.deck['3s'], self.deck['3d'], ]))
        self.assertEqual(hand[4], self.deck['Qd'])

        # Two pair, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['3d'], self.deck['Jh'], self.deck['Qd'], self.deck['Qs'])
        hand = Hands.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['Qd'], self.deck['Qs'], ]))
        self.assertEqual(set(hand[2:4]), set([ self.deck['3s'], self.deck['3d'], ]))
        self.assertEqual(hand[4], self.deck['As'])

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
