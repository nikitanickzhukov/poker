from unittest import TestCase
from collections import Counter

from engine.infrastructure.timer import Timer

from engine.domain.model.card import StandardDeck
from engine.domain.model.game.holdem import Pocket, Board, Preflop, Flop, Turn, River, Identifier


TEST_COUNT = 10000


class StatTestCase(TestCase):
    def test_stat(self):
        timer = Timer()

        count = Counter()
        for _ in range(TEST_COUNT):
            deck = StandardDeck()
            deck.shuffle()
            preflop = Preflop(cards=deck.extract_top_cards(count=Preflop.length))
            pocket = Pocket(streets=(preflop,))
            flop = Flop(cards=deck.extract_top_cards(count=Flop.length))
            turn = Turn(cards=deck.extract_top_cards(count=Turn.length))
            river = River(cards=deck.extract_top_cards(count=River.length))
            board = Board(streets=(flop, turn, river))
            with timer:
                hand = Identifier.identify(pocket, board)
            count.update([hand.__class__])

        for item, c in count.most_common():
            print(item, c)

        print('time:', timer.elapsed)
        print('per second:', round(TEST_COUNT / timer.elapsed))
