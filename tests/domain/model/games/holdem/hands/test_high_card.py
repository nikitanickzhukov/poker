from unittest import TestCase

from domain.model.cards import StandardDeck
from domain.model.games.holdem import (
    Preflop, Flop, Turn, River,
    Pocket, Board, Identifier, HighCard,
)


class HighCardTestCase(TestCase):
    def test_in_pocket(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('As', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '4d', 'Jh')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual([x.code for x in hand], ['As', 'Qd', 'Jh', '6s', '4d'])

    def test_on_board(self):
        deck = StandardDeck()
        preflop = Preflop(cards=deck.extract(('7s', '2s')))
        pocket = Pocket(streets=(preflop,))
        flop = Flop(cards=deck.extract(('3s', '4d', 'Jh')))
        turn = Turn(cards=deck.extract(('Qd',)))
        river = River(cards=deck.extract(('6s',)))
        board = Board(streets=(flop, turn, river))
        hand = Identifier.identify(pocket, board)
        self.assertIsInstance(hand, HighCard)
        self.assertEqual([x.code for x in hand], ['Qd', 'Jh', '7s', '6s', '4d'])
