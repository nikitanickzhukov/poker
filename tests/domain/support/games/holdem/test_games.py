from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.holdem import Player, Layout, Pocket, Board, Dealer, Pot, Identifier, Game


class GameTestCase(TestCase):
    def test_start(self):
        a = Player(nickname='a', chips=10, pocket=Pocket())
        b = Player(nickname='b', chips=20, pocket=Pocket())
        c = Player(nickname='c', chips=30, pocket=Pocket())
        d = Player(nickname='d', chips=40, pocket=Pocket())

        game = Game(
            layout=Layout(players=(a, b, c, d)),
            board=Board(),
            dealer=Dealer(),
            pot=Pot(players=(a, b, c, d), chips=0),
            identifier=Identifier,
            deck=StandardDeck(),
            bb=2,
            sb=1,
        )
        game.run()
