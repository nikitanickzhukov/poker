from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, TwoPair


class TwoPairTestCase(TestCase):
    def test_two_pair(self):
        # Two pair, a pair in the pocket and a pair on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['2h'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([cardset['As'], cardset['Ad']]))
        self.assertEqual(set(hand[2:4]), set([cardset['2s'], cardset['2h']]))
        self.assertEqual(hand[4], cardset['Qd'])

        # Two pair, in the pocket and on the board
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['3d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([cardset['As'], cardset['Ad']]))
        self.assertEqual(set(hand[2:4]), set([cardset['3s'], cardset['3d']]))
        self.assertEqual(hand[4], cardset['Qd'])

        # Two pair, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3d'], cardset['Jh'], cardset['Qd'], cardset['Qs'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([cardset['Qd'], cardset['Qs']]))
        self.assertEqual(set(hand[2:4]), set([cardset['3s'], cardset['3d']]))
        self.assertEqual(hand[4], cardset['As'])
