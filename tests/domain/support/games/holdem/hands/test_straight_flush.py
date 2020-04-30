from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, StraightFlush


class StraightFlushTestCase(TestCase):
    def test_straight_flush(self):
        # Straight flush, wheel, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['2d'], cardset['Jh'], cardset['4s'], cardset['5s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight flush, wheel, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['Ks'], cardset['2s'])
        board = Board(cardset['3s'], cardset['As'], cardset['Jh'], cardset['4s'], cardset['5s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight flush, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['4s'], cardset['7s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['6s'], cardset['5s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['7s'])

        # Straight flush, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ts'], cardset['Js'], cardset['Qs'], cardset['Ks'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['As'])

        # Straight flush, on the board only
        pocket = Pocket(cardset['Ks'], cardset['Js'])
        board = Board(cardset['3s'], cardset['4s'], cardset['5s'], cardset['7s'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['7s'])
