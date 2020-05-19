from typing import Sequence, Type, Optional

from engine.domain.model.card import Card, Deck

from .decision import Decision, Fold, Check, Call, Bet, Raise
from .street import Street
from .board import Board
from .table import Table
from .player import Player
from .pot import Pot
from .hand import Identifier
from .event import (
    BoardCardsDealt, PocketCardsDealt,
    PlayerDrawCommitted, PlayerDecisionCommitted,
)


class Dealer:
    @classmethod
    def shuffle_deck(cls, deck: Deck) -> None:
        deck.shuffle()

    @classmethod
    def collect_ante(cls, table: Table, pot: Pot, ante: int) -> None:
        for player in table.get_players():
            chips = player.post_ante(chips=ante)
            pot.put_chips(chips=chips)

    @classmethod
    def collect_blinds(cls, table: Table, pot: Pot, sb: int, bb: int) -> None:
        player = table.get_sb_player()
        if player:
            chips = player.post_blind(chips=sb)
            pot.put_chips(chips=chips, player=player)
        player = table.get_bb_player()
        if player:
            chips = player.post_blind(chips=bb)
            pot.put_chips(chips=chips, player=player)

    @classmethod
    def deal_board_cards(
        cls,
        board: Board,
        deck: Deck,
        street_class: Type[Street],
        cards: Optional[Sequence[Card]] = None,
    ) -> BoardCardsDealt:
        if cards is None:
            cards = deck.extract_top_cards(count=street_class.length)
        else:
            cards = deck.extract_certain_cards(cards=cards)
        street = street_class(cards=cards)
        board.append(street=street)
        return BoardCardsDealt(cards=cards)

    @classmethod
    def deal_pocket_cards(
        cls,
        player: Player,
        deck: Deck,
        street_class: Type[Street],
        cards: Optional[Sequence[Card]] = None,
    ) -> PocketCardsDealt:
        if cards is None:
            cards = deck.extract_top_cards(count=street_class.length)
        else:
            cards = deck.extract_certain_cards(cards=cards)
        street = street_class(cards=cards)
        player.pocket.append(street=street)
        return PocketCardsDealt(player=player, cards=cards)

    @classmethod
    def handle_draw(
        cls,
        player: Player,
        deck: Deck,
        street_class: Type[Street],
        in_cards: Optional[Sequence[Card]] = None,
        out_cards: Optional[Sequence[Card]] = None,
    ) -> PlayerDrawCommitted:
        assert (out_cards is None) == (in_cards is None), 'In and out cards must be both defined or undefined'
        if out_cards is None:
            out_cards = player.do_draw()
            in_cards = deck.extract_top_cards(count=len(out_cards))
        player.pocket.draw_cards(in_cards=in_cards, out_cards=out_cards)
        return PlayerDrawCommitted(player=player, in_cards=in_cards, out_cards=out_cards)

    @classmethod
    def handle_decision(
        cls,
        player: Player,
        street_class: Type[Street],
        pot: Pot,
        decision: Optional[Decision] = None,
    ) -> PlayerDecisionCommitted:
        if decision is None:
            decision = player.do_decision()
        if isinstance(decision, Fold):
            player.fold()
            pot.remove_player(player=player)
        elif isinstance(decision, Check):
            pass
        elif isinstance(decision, Call):
            chips = player.post_bet(chips=decision.chips)
            pot.put_chips(player=player, chips=chips)
        elif isinstance(decision, Bet):
            chips = player.post_bet(chips=decision.chips)
            pot.put_chips(player=player, chips=chips)
        elif isinstance(decision, Raise):
            chips = player.post_bet(chips=decision.chips)
            pot.put_chips(player=player, chips=chips)
        else:
            raise TypeError(decision)
        return PlayerDecisionCommitted(player=player, decision=decision)

    @classmethod
    def define_winner(
        cls,
        table: Table,
        board: Board,
        pot: Pot,
        identifier: Identifier,
    ) -> None:
        best = None
        for player in table.get_players():
            if player.is_folded():
                continue
            hand = identifier.identify(player.pocket, board)
            if best is None or hand > best[1]:
                if best:
                    best[0].fold()
                best = player, hand
            elif hand < best[1]:
                player.fold()


__all__ = ('Dealer',)
