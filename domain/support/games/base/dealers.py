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
from .events import Seat, Deal, Decision, History
from .hands import Identifier


class Dealer(ABC):
    def __init__(self):
        self._pocket_dealt = defaultdict(dict)
        self._board_dealt = {}
        self._current_event = None
        self._current_street = None
        self._current_player = None

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
        for event in history:
            self._current_event = event.__class__

            if isinstance(event, Seat):
                player = player_class(pocket=pocket_class(), nickname=event.nickname, chips=event.chips)
                table.seat_player(player=player)
                pot.add_player(player=player)
                self._current_street = None
                self._current_player = player
            elif isinstance(event, Deal):
                cards = deck.extract(tuple(event.cards))
                street_class = self._get_street_class(event.street, street_classes)
                street = street_class(cards=cards)
                if event.nickname:
                    player = table[event.nickname]
                    player.pocket.append(street)
                    self._current_player = player
                else:
                    board.append(street)
                    self._current_player = None
                self._current_street = street_class
            elif isinstance(event, Decision):
                player = table[event.nickname]
                street_class = self._get_street_class(event.street, street_classes)
                action_class = self._get_action_class(event.action)
                action = action_class(chips=event.chips)
                self._process_action(player=player, street_class=street_class, action=action, pot=pot)
                self._current_street = street_class
                self._current_player = player
            else:
                raise TypeError(event)

        print('Pocket dealt', self._pocket_dealt)
        print('Board dealt', self._board_dealt)
        print('Current street', self._current_street)
        print('Current player', self._current_player)

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

    def _process_action(self, action: Action, street_class: Type[Street], player: Player, pot: Pot) -> None:
        print(repr(player), repr(action), street_class)

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
