from unittest import TestCase
from collections import Counter

from utils.timer import Timer

from domain.generic.cards import StandardDeck
from domain.support.games.omaha import Pocket, Board, Identifier


TEST_COUNT = 10000


class StatTestCase(TestCase):
    def test_stat(self):
        timer = Timer()

        count = Counter()
        for i in range(TEST_COUNT):
            deck = StandardDeck()
            deck.shuffle()
            pocket = Pocket(deck.pop(), deck.pop(), deck.pop(), deck.pop())
            board = Board(deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop())
            with timer:
                hand = Identifier.identify(pocket, board)
            count.update([hand.__class__])

        for item, c in count.most_common():
            print(item, c)

        print('time:', timer.elapsed)
        print('per second:', round(TEST_COUNT / timer.elapsed))
