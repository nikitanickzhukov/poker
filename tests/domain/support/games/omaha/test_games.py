from unittest import TestCase

from domain.generic.cards import StandardDeck
from domain.support.games.omaha import History, Seat, Deal, Decision, Game


class GameTestCase(TestCase):
    def test_start(self):
        history = History(events=(
            Seat(nickname='a', chips=10),
            Seat(nickname='b', chips=20),
            Seat(nickname='c', chips=30),
            Seat(nickname='d', chips=40),
            Deal(street='Preflop', cards=('Ah', 'Kc', 'Tc', 'Ts'), nickname='a'),
            Deal(street='Preflop', cards=('7h', '8h', '4s', '5s'), nickname='b'),
            Deal(street='Preflop', cards=('3c', '3s', '6d', '6h'), nickname='c'),
            Deal(street='Preflop', cards=('Jc', 'Jh', '7s', '9s'), nickname='d'),
            Decision(nickname='a', street='Preflop', action='Blind', chips=1),
            Decision(nickname='b', street='Preflop', action='Blind', chips=2),
            Decision(nickname='c', street='Preflop', action='Raise', chips=4),
            Decision(nickname='d', street='Preflop', action='Call', chips=4),
            Decision(nickname='a', street='Preflop', action='Call', chips=3),
            Decision(nickname='b', street='Preflop', action='Call', chips=2),
            Deal(street='Flop', cards=('Th', '9c', '5c')),
        ))

        game = Game(history=history, deck=StandardDeck())
        game.run()
