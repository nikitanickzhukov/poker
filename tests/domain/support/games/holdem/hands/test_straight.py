from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, Straight


class StraightTestCase(TestCase):
    def test_straight(self):
        # Straight, wheel, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['2d'], cardset['Jh'], cardset['4d'], cardset['5s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight, wheel, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['Ks'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['4d'], cardset['5s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['4s'], cardset['7s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['6d'], cardset['5s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['7s'])

        # Straight, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Td'], cardset['Jh'], cardset['Qd'], cardset['Ks'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['As'])

        # Straight, on the board only
        pocket = Pocket(cardset['Ks'], cardset['Js'])
        board = Board(cardset['3s'], cardset['4d'], cardset['5h'], cardset['7d'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['7d'])
