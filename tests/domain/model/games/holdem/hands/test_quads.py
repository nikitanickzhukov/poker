from unittest import TestCase

from domain.model.cards import StandardDeck
from domain.model.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, Quads,
)


class QuadsTestCase(TestCase):
    def test_pp(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', 'Ad')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ac', 'Ah')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual([x.code for x in hand], ['As', 'Ah', 'Ad', 'Ac', 'Qd'])

    def test_board_trips(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', 'Ac', 'Ad')))
        turn = Turn(cards=deck.extract(('Ah',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual([x.code for x in hand], ['As', 'Ah', 'Ad', 'Ac', '6s'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '3c', '3h')))
        turn = Turn(cards=deck.extract(('3d',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, Quads)
        self.assertEqual([x.code for x in hand], ['3s', '3h', '3d', '3c', 'As'])
