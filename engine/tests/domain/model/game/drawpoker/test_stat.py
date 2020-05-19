from unittest import TestCase
from collections import Counter

from engine.infrastructure.timer import Timer

from engine.domain.model.card import StandardDeck
from engine.domain.model.game.drawpoker import Pocket, Board, PreDraw, Draw, Identifier


TEST_COUNT = 10000


class StatTestCase(TestCase):
    def test_stat(self):
        timer = Timer()

        count = Counter()
        for _ in range(TEST_COUNT):
            deck = StandardDeck()
            deck.shuffle()
            predraw = PreDraw(cards=deck.extract_top_cards(count=PreDraw.length))
            pocket = Pocket(streets=(predraw,))
            draw = Draw(cards=())
            board = Board(streets=(draw,))
            with timer:
                hand = Identifier.identify(pocket, board)
            count.update([hand.__class__])

        for item, c in count.most_common():
            print(item, c)

        print('time:', timer.elapsed)
        print('per second:', round(TEST_COUNT / timer.elapsed))
