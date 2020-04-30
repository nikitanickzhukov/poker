from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, HighCard


class HighCardTestCase(TestCase):
    def test_high_card(self):
        # High card in the pocket
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[1], cardset['Qd'])

        # High card on the board
        pocket = Pocket(cardset['7s'], cardset['2s'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['Qd'])
        self.assertEqual(hand[1], cardset['Jh'])
