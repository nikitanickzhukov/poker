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
        pocket = Pocket(self.deck['As'], self.deck['2s'], self.deck['4d'], self.deck['3c'])
        board = Board(self.deck['Qs'], self.deck['7d'], self.deck['Jh'], self.deck['Kd'], self.deck['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['As'])
        self.assertEqual(hand[1], self.deck['Kd'])
        self.assertIn(self.deck['4d'], hand)

        # High card on the board
        pocket = Pocket(self.deck['7s'], self.deck['2s'], self.deck['6c'], self.deck['Tc'])
        board = Board(self.deck['3s'], self.deck['4d'], self.deck['Jh'], self.deck['Qd'], self.deck['8s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], self.deck['Qd'])
        self.assertEqual(hand[1], self.deck['Jh'])
        self.assertIn(self.deck['Tc'], hand)
        self.assertIn(self.deck['7s'], hand)

    def test_speed(self):
        start = datetime.now()

        test_count = 10000
        count = Counter()
        for i in range(test_count):
            self.deck.shuffle()
            pocket = Pocket(*self.deck[0:4])
            board = Board(*self.deck[4:9])
            hand = HandIdentifier.identify(pocket, board)
            count.update([hand.__class__])

        duration = datetime.now() - start
        for item, c in count.most_common():
            print(item, c)
        print('time', duration)
        print('per second', round(test_count / duration.total_seconds()))


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
