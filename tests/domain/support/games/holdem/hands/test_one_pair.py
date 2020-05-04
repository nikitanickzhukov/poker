from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, OnePair


class OnePairTestCase(TestCase):
    def test_one_pair(self):
        # One pair, in the pocket and on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([cardset['As'], cardset['Ad']]))
        self.assertEqual(hand[2], cardset['Qd'])

        # One pair, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['4s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([cardset['4d'], cardset['4s']]))
        self.assertEqual(hand[2], cardset['As'])

        # One pair, in the pocket only
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([cardset['As'], cardset['Ad']]))
        self.assertEqual(hand[2], cardset['Qd'])
