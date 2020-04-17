from unittest import TestCase
from datetime import datetime
from collections import Counter

from cards import StandardDeck
from .pockets import Pocket
from .boards import Board
from .hands import HandIdentifier, HighCard, OnePair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush
from .players import Player
from .rounds import Round


class IdentifyTestCase(TestCase):
    def setUp(self):
        self.deck = StandardDeck()
        self.deck.shuffle()

    def tearDown(self):
        del self.deck

    def test_high_card(self):
        # High card in the pocket
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['As'])
        self.assertEqual(hand[1], self.deck['Qd'])

        # High card on the board
        pocket = Pocket(self.deck['7s'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['Qd'])
        self.assertEqual(hand[1], self.deck['Jh'])

    def test_one_pair(self):
        # One pair, in the pocket and on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'] ]))
        self.assertEqual(hand[2], self.deck['Qd'])

        # One pair, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['4s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['4d'], self.deck['4s'] ]))
        self.assertEqual(hand[2], self.deck['As'])

        # One pair, in the pocket only
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'] ]))
        self.assertEqual(hand[2], self.deck['Qd'])

    def test_two_pair(self):
        # Two pair, a pair in the pocket and a pair on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['2h'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'] ]))
        self.assertEqual(set(hand[2:4]), set([ self.deck['2s'], self.deck['2h'] ]))
        self.assertEqual(hand[4], self.deck['Qd'])

        # Two pair, in the pocket and on the board
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['3d'], self.deck['Jh'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['As'], self.deck['Ad'] ]))
        self.assertEqual(set(hand[2:4]), set([ self.deck['3s'], self.deck['3d'] ]))
        self.assertEqual(hand[4], self.deck['Qd'])

        # Two pair, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['3d'], self.deck['Jh'], self.deck['Qd'], self.deck['Qs'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ self.deck['Qd'], self.deck['Qs'] ]))
        self.assertEqual(set(hand[2:4]), set([ self.deck['3s'], self.deck['3d'] ]))
        self.assertEqual(hand[4], self.deck['As'])

    def test_trips(self):
        # Trips, 1 in the pocket and 2 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Ac'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ self.deck['As'], self.deck['Ad'], self.deck['Ac'] ]))
        self.assertEqual(hand[3], self.deck['Qd'])

        # Trips, a set
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['2d'], self.deck['Ac'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ self.deck['As'], self.deck['Ad'], self.deck['Ac'] ]))
        self.assertEqual(hand[3], self.deck['Qd'])

        # Trips, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['3d'], self.deck['3c'], self.deck['Qd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ self.deck['3s'], self.deck['3d'], self.deck['3c'] ]))
        self.assertEqual(hand[3], self.deck['As'])

    def test_straight(self):
        # Straight, wheel, 2 in the pocket and 3 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['2d'], self.deck['Jh'], self.deck['4d'], self.deck['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], self.deck['5s'])

        # Straight, wheel, 1 in the pocket and 4 on the board
        pocket = Pocket(self.deck['Ks'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Jh'], self.deck['4d'], self.deck['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], self.deck['5s'])

        # Straight, 2 in the pocket and 3 on the board
        pocket = Pocket(self.deck['4s'], self.deck['7s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Jh'], self.deck['6d'], self.deck['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], self.deck['7s'])

        # Straight, 1 in the pocket and 4 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Td'], self.deck['Jh'], self.deck['Qd'], self.deck['Ks'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], self.deck['As'])

        # Straight, on the board only
        pocket = Pocket(self.deck['Ks'], self.deck['Js'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['5h'], self.deck['7d'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], self.deck['7d'])

    def test_flush(self):
        # Flush, 2 in the pocket and 3 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Ac'], self.deck['Qs'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], self.deck['As'])
        self.assertEqual(hand[4], self.deck['2s'])

        # Flush, 1 in the pocket and 4 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Js'], self.deck['Qs'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], self.deck['As'])
        self.assertEqual(hand[4], self.deck['3s'])

        # Flush, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3d'], self.deck['Ad'], self.deck['Jd'], self.deck['Qd'], self.deck['6d'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], self.deck['Ad'])
        self.assertEqual(hand[4], self.deck['3d'])

    def test_full_house(self):
        # Full house, a set and a pair on the board
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['Ac'], self.deck['3c'], self.deck['2d'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ self.deck['As'], self.deck['Ad'], self.deck['Ac'] ]))
        self.assertEqual(set(hand[3:5]), set([ self.deck['3s'], self.deck['3c'] ]))

        # Full house, a trips and a pair on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ac'], self.deck['2c'], self.deck['2d'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ self.deck['2s'], self.deck['2d'], self.deck['2c'] ]))
        self.assertEqual(set(hand[3:5]), set([ self.deck['As'], self.deck['Ac'] ]))

        # Full house, a pocket pair and a trips on the board
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['3c'], self.deck['3d'], self.deck['2d'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ self.deck['3s'], self.deck['3d'], self.deck['3c'] ]))
        self.assertEqual(set(hand[3:5]), set([ self.deck['As'], self.deck['Ad'] ]))

        # Full house, on the board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['3c'], self.deck['3d'], self.deck['6d'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ self.deck['3s'], self.deck['3d'], self.deck['3c'] ]))
        self.assertEqual(set(hand[3:5]), set([ self.deck['6d'], self.deck['6s'] ]))

    def test_quads(self):
        # Quads, a pocket pair
        pocket = Pocket(self.deck['As'], self.deck['Ad'])
        board = Board(self.deck['3s'], self.deck['Ac'], self.deck['Ah'], self.deck['Jh'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ self.deck['As'], self.deck['Ad'], self.deck['Ac'], self.deck['Ah'] ]))
        self.assertEqual(hand[4], self.deck['Jh'])

        # Quads, a trips on a board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ac'], self.deck['Ah'], self.deck['Ad'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ self.deck['As'], self.deck['Ad'], self.deck['Ac'], self.deck['Ah'] ]))
        self.assertEqual(hand[4], self.deck['6s'])

        # Quads, on a board only
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['3c'], self.deck['3h'], self.deck['3d'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ self.deck['3s'], self.deck['3d'], self.deck['3c'], self.deck['3h'] ]))
        self.assertEqual(hand[4], self.deck['As'])

    def test_straight_flush(self):
        # Straight flush, wheel, 2 in the pocket and 3 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['2d'], self.deck['Jh'], self.deck['4s'], self.deck['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], self.deck['5s'])

        # Straight flush, wheel, 1 in the pocket and 4 on the board
        pocket = Pocket(self.deck['Ks'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['As'], self.deck['Jh'], self.deck['4s'], self.deck['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], self.deck['5s'])

        # Straight flush, 2 in the pocket and 3 on the board
        pocket = Pocket(self.deck['4s'], self.deck['7s'])
        board = Board(self.deck['3s'], self.deck['Ad'], self.deck['Jh'], self.deck['6s'], self.deck['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], self.deck['7s'])

        # Straight flush, 1 in the pocket and 4 on the board
        pocket = Pocket(self.deck['As'], self.deck['2s'])
        board = Board(self.deck['3s'], self.deck['Ts'], self.deck['Js'], self.deck['Qs'], self.deck['Ks'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], self.deck['As'])

        # Straight flush, on the board only
        pocket = Pocket(self.deck['Ks'], self.deck['Js'])
        board = Board(self.deck['3s'], self.deck['4s'], self.deck['5s'], self.deck['7s'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], self.deck['7s'])

    def test_speed(self):
        start = datetime.now()

        test_count = 10000
        count = Counter()
        for i in range(test_count):
            self.deck.shuffle()
            pocket = Pocket(*self.deck[0:2])
            board = Board(*self.deck[2:7])
            hand = HandIdentifier.identify(pocket, board)
            count.update([hand.__class__])

        duration = datetime.now() - start
        for item, c in count.most_common():
            print(item, c)
        print('time:', duration)
        print('per second:', round(test_count / duration.total_seconds()))


class RoundTestCase(TestCase):
    def setUp(self):
        a = Player(nickname='a', chips=10)
        b = Player(nickname='b', chips=20)
        c = Player(nickname='c', chips=30)
        d = Player(nickname='d', chips=40)
        self.players = (a, b, c, d)

    def test_init(self):
        r = Round(players=self.players, bb=2, sb=1)
        r.start()
