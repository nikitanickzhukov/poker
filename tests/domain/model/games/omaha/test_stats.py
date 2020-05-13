from unittest import TestCase
from collections import Counter

from utils.timer import Timer

from domain.model.cards import StandardDeck
from domain.model.games.omaha import Pocket, Board, Preflop, Flop, Turn, River, Identifier


TEST_COUNT = 10000


class StatTestCase(TestCase):
    def test_stat(self):
        timer = Timer()

        count = Counter()
        for _ in range(TEST_COUNT):
            deck = StandardDeck()
            deck.shuffle()
            preflop = Preflop(cards=deck.extract(slice(0, 4)))
            pocket = Pocket(streets=(preflop,))
            flop = Flop(cards=deck.extract(slice(0, 3)))
            turn = Turn(cards=(deck.extract(0),))
            river = River(cards=(deck.extract(0),))
            board = Board(streets=(flop, turn, river))
            with timer:
                hand = Identifier.identify(pocket, board)
            count.update([hand.__class__])

        for item, c in count.most_common():
            print(item, c)

        print('time:', timer.elapsed)
        print('per second:', round(TEST_COUNT / timer.elapsed))
