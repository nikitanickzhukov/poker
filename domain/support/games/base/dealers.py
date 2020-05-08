from abc import ABC
from typing import Sequence, Type
from collections import defaultdict

from domain.generic.cards import Deck

from .actions import Action, Ante, Blind, Fold, Check, Call, Bet, Raise, AllIn
from .streets import Street
from .boards import Board
from .pockets import Pocket
from .tables import Player, Table
from .pots import Pot
from .histories import Seat, PocketDeal, BoardDeal, Decision, History
from .hands import Identifier


class Dealer(ABC):
    def shuffle_deck(self, deck: Deck) -> None:
        deck.shuffle()

    def restore_state(
        self,
        street_classes: Sequence[Type[Street]],
        player_class: Type[Player],
        pocket_class: Type[Pocket],
        history: History,
        deck: Deck,
        table: Table,
        board: Board,
        pot: Pot,
    ) -> None:
        for item in history:
            if isinstance(item, Seat):
                player = player_class(pocket=pocket_class(), nickname=item.nickname, chips=item.chips)
                table.seat_player(player=player)
                pot.add_player(player=player)
            elif isinstance(item, PocketDeal):
                cards = deck.extract(tuple(item.cards))
                street_class = self._get_street_class(item.street, street_classes)
                street = street_class(cards=cards)
                player = table[item.nickname]
                player.pocket.append(street)
            elif isinstance(item, BoardDeal):
                cards = deck.extract(tuple(item.cards))
                street_class = self._get_street_class(item.street, street_classes)
                street = street_class(cards=cards)
                board.append(street)
            elif isinstance(item, Decision):
                player = table[item.nickname]
                action_class = self._get_action_class(item.action)
                action = action_class(chips=item.chips)
                self._process_action(player=player, action=action, pot=pot)
            else:
                raise TypeError(item)

    def process(
        self,
        street_classes: Sequence[Type[Street]],
        history: History,
        deck: Deck,
        table: Table,
        board: Board,
        pot: Pot,
    ) -> None:
        pass

    def showdown(
        self,
        table: Table,
        board: Board,
        pot: Pot,
        identifier: Identifier,
    ) -> None:
        print(repr(board))
        for player in table.active_players:
            hand = identifier.identify(player.pocket, board)
            print(player, ' == ', repr(hand))
        print(repr(pot))

    def _process_action(self, action: Action, player: Player, pot: Pot) -> None:
        print(repr(player), repr(action))

        if isinstance(action, Ante):
            pot.add_chips(action.chips)
        elif isinstance(action, Blind):
            pot.add_chips(action.chips)
        elif isinstance(action, Fold):
            pot.remove_player(player)
        elif isinstance(action, Check):
            pass
        elif isinstance(action, Call):
            pot.add_chips(action.chips)
        elif isinstance(action, Bet):
            pot.add_chips(action.chips)
        elif isinstance(action, Raise):
            pot.add_chips(action.chips)
        elif isinstance(action, AllIn):
            pot.add_chips(action.chips)

    def _deal_board_cards(self, street_class: Type[Street], board: Board, deck: Deck) -> None:
        idx = slice(len(deck) - street_class.length, len(deck))
        cards = deck.extract(idx)
        street = street_class(cards=cards)
        board.append(street)

    def _deal_pocket_cards(self, street_class: Type[Street], table: Table, deck: Deck) -> None:
        for player in table.active_players:
            idx = slice(len(deck) - street_class.length, len(deck))
            cards = deck.extract(idx)
            street = street_class(cards=cards)
            player.pocket.append(street)

    def _get_street_class(self, name: str, classes: Sequence[Type[Street]]) -> Type[Street]:
        for cls in classes:
            if cls.__name__ == name:
                return cls
        raise KeyError(name)

    def _get_action_class(self, name: str) -> Type[Action]:
        return globals()[name]


__all__ = ('Dealer',)
