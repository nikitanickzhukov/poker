from unittest import TestCase

from domain.generic.cards import cardset
from domain.support.games.holdem import Pocket, Board, Identifier, Trips


class TripsTestCase(TestCase):
    def test_trips(self):
        # Trips, 1 in the pocket and 2 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Ac'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ cardset['As'], cardset['Ad'], cardset['Ac'] ]))
        self.assertEqual(hand[3], cardset['Qd'])

        # Trips, a set
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['2d'], cardset['Ac'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ cardset['As'], cardset['Ad'], cardset['Ac'] ]))
        self.assertEqual(hand[3], cardset['Qd'])

        # Trips, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3d'], cardset['3c'], cardset['Qd'], cardset['6s'])
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ cardset['3s'], cardset['3d'], cardset['3c'] ]))
        self.assertEqual(hand[3], cardset['As'])
