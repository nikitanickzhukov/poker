from unittest import TestCase

from domain.cards import StandardDeck
from domain.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Flush,
)


class FlushTestCase(TestCase):
    def test_2_pocket_3_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', 'Ac')))
        turn = Turn(cards=deck.extract(('Qs',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual([x.code for x in hand], ['As', 'Qs', '6s', '3s', '2s'])

    def test_1_pocket_4_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ad', 'Js')))
        turn = Turn(cards=deck.extract(('Qs',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual([x.code for x in hand], ['As', 'Qs', 'Js', '6s', '3s'])

    def test_5_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3d', 'Ad', 'Jd')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6d',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Flush)
        self.assertEqual([x.code for x in hand], ['Ad', 'Qd', 'Jd', '6d', '3d'])
