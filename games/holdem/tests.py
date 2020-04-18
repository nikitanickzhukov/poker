from unittest import TestCase
from collections import Counter

from utils.timer import Timer
from cards import StandardDeck, cardset
from .pockets import Pocket
from .boards import Board
from .hands import HandIdentifier, HighCard, OnePair, TwoPair, Trips, Straight, Flush, FullHouse, Quads, StraightFlush
from .players import Player
from .rounds import Round


SPEED_TEST_COUNT = 10000


class IdentifyTestCase(TestCase):
    def test_high_card(self):
        # High card in the pocket
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[1], cardset['Qd'])

        # High card on the board
        pocket = Pocket(cardset['7s'], cardset['2s'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['Qd'])
        self.assertEqual(hand[1], cardset['Jh'])

    def test_one_pair(self):
        # One pair, in the pocket and on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ cardset['As'], cardset['Ad'] ]))
        self.assertEqual(hand[2], cardset['Qd'])

        # One pair, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['4s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ cardset['4d'], cardset['4s'] ]))
        self.assertEqual(hand[2], cardset['As'])

        # One pair, in the pocket only
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, OnePair)
        self.assertEqual(set(hand[0:2]), set([ cardset['As'], cardset['Ad'] ]))
        self.assertEqual(hand[2], cardset['Qd'])

    def test_two_pair(self):
        # Two pair, a pair in the pocket and a pair on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['2h'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ cardset['As'], cardset['Ad'] ]))
        self.assertEqual(set(hand[2:4]), set([ cardset['2s'], cardset['2h'] ]))
        self.assertEqual(hand[4], cardset['Qd'])

        # Two pair, in the pocket and on the board
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['3d'], cardset['Jh'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ cardset['As'], cardset['Ad'] ]))
        self.assertEqual(set(hand[2:4]), set([ cardset['3s'], cardset['3d'] ]))
        self.assertEqual(hand[4], cardset['Qd'])

        # Two pair, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3d'], cardset['Jh'], cardset['Qd'], cardset['Qs'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, TwoPair)
        self.assertEqual(set(hand[0:2]), set([ cardset['Qd'], cardset['Qs'] ]))
        self.assertEqual(set(hand[2:4]), set([ cardset['3s'], cardset['3d'] ]))
        self.assertEqual(hand[4], cardset['As'])

    def test_trips(self):
        # Trips, 1 in the pocket and 2 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Ac'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ cardset['As'], cardset['Ad'], cardset['Ac'] ]))
        self.assertEqual(hand[3], cardset['Qd'])

        # Trips, a set
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['2d'], cardset['Ac'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ cardset['As'], cardset['Ad'], cardset['Ac'] ]))
        self.assertEqual(hand[3], cardset['Qd'])

        # Trips, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3d'], cardset['3c'], cardset['Qd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Trips)
        self.assertEqual(set(hand[0:3]), set([ cardset['3s'], cardset['3d'], cardset['3c'] ]))
        self.assertEqual(hand[3], cardset['As'])

    def test_straight(self):
        # Straight, wheel, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['2d'], cardset['Jh'], cardset['4d'], cardset['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight, wheel, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['Ks'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['4d'], cardset['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['4s'], cardset['7s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['6d'], cardset['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['7s'])

        # Straight, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Td'], cardset['Jh'], cardset['Qd'], cardset['Ks'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['As'])

        # Straight, on the board only
        pocket = Pocket(cardset['Ks'], cardset['Js'])
        board = Board(cardset['3s'], cardset['4d'], cardset['5h'], cardset['7d'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Straight)
        self.assertEqual(hand[0], cardset['7d'])

    def test_flush(self):
        # Flush, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Ac'], cardset['Qs'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[4], cardset['2s'])

        # Flush, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Js'], cardset['Qs'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[4], cardset['3s'])

        # Flush, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3d'], cardset['Ad'], cardset['Jd'], cardset['Qd'], cardset['6d'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual(hand[0], cardset['Ad'])
        self.assertEqual(hand[4], cardset['3d'])

    def test_full_house(self):
        # Full house, a set and a pair on the board
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['3c'], cardset['2d'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['As'], cardset['Ad'], cardset['Ac'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['3s'], cardset['3c'] ]))

        # Full house, a trips and a pair on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['2c'], cardset['2d'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['2s'], cardset['2d'], cardset['2c'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['As'], cardset['Ac'] ]))

        # Full house, a pocket pair and a trips on the board
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['3c'], cardset['3d'], cardset['2d'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['3s'], cardset['3d'], cardset['3c'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['As'], cardset['Ad'] ]))

        # Full house, on the board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3c'], cardset['3d'], cardset['6d'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, FullHouse)
        self.assertEqual(set(hand[0:3]), set([ cardset['3s'], cardset['3d'], cardset['3c'] ]))
        self.assertEqual(set(hand[3:5]), set([ cardset['6d'], cardset['6s'] ]))

    def test_quads(self):
        # Quads, a pocket pair
        pocket = Pocket(cardset['As'], cardset['Ad'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['Ah'], cardset['Jh'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ cardset['As'], cardset['Ad'], cardset['Ac'], cardset['Ah'] ]))
        self.assertEqual(hand[4], cardset['Jh'])

        # Quads, a trips on a board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ac'], cardset['Ah'], cardset['Ad'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ cardset['As'], cardset['Ad'], cardset['Ac'], cardset['Ah'] ]))
        self.assertEqual(hand[4], cardset['6s'])

        # Quads, on a board only
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['3c'], cardset['3h'], cardset['3d'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual(set(hand[0:4]), set([ cardset['3s'], cardset['3d'], cardset['3c'], cardset['3h'] ]))
        self.assertEqual(hand[4], cardset['As'])

    def test_straight_flush(self):
        # Straight flush, wheel, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['2d'], cardset['Jh'], cardset['4s'], cardset['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight flush, wheel, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['Ks'], cardset['2s'])
        board = Board(cardset['3s'], cardset['As'], cardset['Jh'], cardset['4s'], cardset['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['5s'])

        # Straight flush, 2 in the pocket and 3 on the board
        pocket = Pocket(cardset['4s'], cardset['7s'])
        board = Board(cardset['3s'], cardset['Ad'], cardset['Jh'], cardset['6s'], cardset['5s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['7s'])

        # Straight flush, 1 in the pocket and 4 on the board
        pocket = Pocket(cardset['As'], cardset['2s'])
        board = Board(cardset['3s'], cardset['Ts'], cardset['Js'], cardset['Qs'], cardset['Ks'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['As'])

        # Straight flush, on the board only
        pocket = Pocket(cardset['Ks'], cardset['Js'])
        board = Board(cardset['3s'], cardset['4s'], cardset['5s'], cardset['7s'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, StraightFlush)
        self.assertEqual(hand[0], cardset['7s'])

    def test_speed(self):
        timer = Timer()

        count = Counter()
        for i in range(SPEED_TEST_COUNT):
            deck = StandardDeck()
            deck.shuffle()
            pocket = Pocket(deck.pop(), deck.pop())
            board = Board(deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop())
            with timer:
                hand = HandIdentifier.identify(pocket, board)
            count.update([hand.__class__])

        for item, c in count.most_common():
            print(item, c)
        print('time:', timer.elapsed)
        print('per second:', round(SPEED_TEST_COUNT / timer.elapsed))


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
