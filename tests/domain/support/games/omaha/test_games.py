from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.omaha import History, Seat, PocketDeal, BoardDeal, Decision, Game


class GameTestCase(TestCase):
    def test_start(self):
        history = History(events=(
            Seat(nickname='a', chips=10),
            Seat(nickname='b', chips=20),
            Seat(nickname='c', chips=30),
            Seat(nickname='d', chips=40),
            PocketDeal(nickname='a', street='Preflop', cards=('Ah', 'Kc', 'Tc', 'Ts')),
            PocketDeal(nickname='b', street='Preflop', cards=('7h', '8h', '4s', '5s')),
            PocketDeal(nickname='c', street='Preflop', cards=('3c', '3s', '6d', '6h')),
            PocketDeal(nickname='d', street='Preflop', cards=('Jc', 'Jh', '7s', '9s')),
            Decision(nickname='a', action='Blind', chips=1),
            Decision(nickname='b', action='Blind', chips=2),
            Decision(nickname='c', action='Raise', chips=4),
            Decision(nickname='d', action='Call', chips=4),
            Decision(nickname='a', action='Call', chips=3),
            Decision(nickname='b', action='Call', chips=2),
            BoardDeal(street='Flop', cards=('Th', '9c', '5c')),
        ))

        game = Game(history=history, deck=StandardDeck())
        game.run()
