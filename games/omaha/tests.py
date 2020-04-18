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
        pocket = Pocket(cardset['As'], cardset['2s'], cardset['4d'], cardset['3c'])
        board = Board(cardset['Qs'], cardset['7d'], cardset['Jh'], cardset['Kd'], cardset['6s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['As'])
        self.assertEqual(hand[1], cardset['Kd'])
        self.assertIn(cardset['4d'], hand)

        # High card on the board
        pocket = Pocket(cardset['7s'], cardset['2s'], cardset['6c'], cardset['Tc'])
        board = Board(cardset['3s'], cardset['4d'], cardset['Jh'], cardset['Qd'], cardset['8s'])
        hand = HandIdentifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual(hand[0], cardset['Qd'])
        self.assertEqual(hand[1], cardset['Jh'])
        self.assertIn(cardset['Tc'], hand)
        self.assertIn(cardset['7s'], hand)

    def test_speed(self):
        timer = Timer()

        count = Counter()
        for i in range(SPEED_TEST_COUNT):
            deck = StandardDeck()
            deck.shuffle()
            pocket = Pocket(deck.pop(), deck.pop(), deck.pop(), deck.pop())
            board = Board(deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop())
            with timer:
                hand = HandIdentifier.identify(pocket, board)
            count.update([hand.__class__])

        for item, c in count.most_common():
            print(item, c)
        print('time', timer.elapsed)
        print('per second', round(SPEED_TEST_COUNT / timer.elapsed))


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
