from unittest import TestCase

from engine.domain.model.card import cards52 as c52
from engine.domain.model.game.drawpoker import (
    Pocket, Player, Table, Draw,
    Fold, Check, Call, Bet, Raise,
    History, BoardCardsDealt, PocketCardsDealt, PlayerDecisionCommitted, RoundStateChanged,
    DrawPokerRound, TripleDrawPokerRound
)


class RoundTestCase(TestCase):
    def test_start(self):
        a = Player(nickname='a', chips=10, pocket=Pocket())
        b = Player(nickname='b', chips=20, pocket=Pocket())
        c = Player(nickname='c', chips=30, pocket=Pocket())
        d = Player(nickname='d', chips=40, pocket=Pocket())

        table = Table(players=(a, b, c, d))


        history = History(events=(
            PocketCardsDealt(player=a, cards=c52.get_many(codes=('Ah', 'Kc', 'Tc', 'Ts', 'Th'))),
            PocketCardsDealt(player=b, cards=c52.get_many(codes=('7s', '8s', '4s', '5s', 'Th'))),
            PocketCardsDealt(player=c, cards=(c52.get('3c'), c52.get('3s'), c52.get('6d'), c52.get('6h'), c52.get('As'))),
            PocketCardsDealt(player=d, cards=(c52.get('Jc'), c52.get('Jh'), c52.get('7s'), c52.get('9s'), c52.get('8s'))),
            PlayerDecisionCommitted(player=c, decision=Raise(chips=4)),
            PlayerDecisionCommitted(player=d, decision=Call(chips=4)),
            PlayerDecisionCommitted(player=a, decision=Call(chips=3)),
            PlayerDecisionCommitted(player=b, decision=Call(chips=2)),
            RoundStateChanged(street_class=Draw),
        ))

        dp1_round = DrawPokerRound(
            table=table,
            history=history,
            sb=1,
            bb=2,
        )
        dp1_round.run()
