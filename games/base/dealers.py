from typing import List

from cards import Deck
from .streets import Street
from .boards import Board
from .actions import Fold, Check, Call, Bet
from .players import Player
from .pots import Pot


class Dealer():
    def shuffle_deck(self, deck:Deck) -> None:
        deck.shuffle()

    def deal_cards(self, street:Street, board:Board, players:List[Player], deck:Deck) -> None:
        if self._is_board_street(street, board):
            self._deal_board_cards(street, board, deck)
            print(repr(board))
        else:
            self._deal_pocket_cards(street, players, deck)
            for player in players:
                print(repr(player))

    def request_actions(self, street:Street, board:Board, players:List[Player], pot:Pot) -> None:
        print(repr(street))

        idx = self._define_start_idx(street, players)

        bet = 0
        step = 0
        called = 0

        while called != len(self._get_active_players(players)):
            player = players[idx]

            if not player.is_active:
                continue

            action = player.do_action(street, board)

            print(player, repr(action))

            if isinstance(action, Fold):
                player.leave_round()
                pot.remove_player(player)
            elif isinstance(action, Check):
                if bet:
                    raise RuntimeError('Cannot check when there was a bet')
                called += 1
            elif isinstance(action, Call):
                if not bet:
                    raise RuntimeError('Cannot call when there was not a bet')
                player.lose_chips(action.chips)
                pot.add_chips(action.chips)
                called += 1
            elif isinstance(action, Bet):
                if action.chips - bet < step:
                    raise RuntimeError('Cannot bet less than step')
                player.lose_chips(action.chips)
                pot.add_chips(action.chips)
                step = action.chips - bet
                bet = action.chips
                called = 1

            idx = idx + 1
            if idx == len(players):
                idx = 0

    def showdown(self, board:Board, players:List[Player], pot:Pot, hand_class:type) -> None:
        print(repr(board))
        for player in self._get_active_players(players):
            hand = hand_class.identify(player.pocket, board)
            print(player, ' == ', repr(hand))
        print(repr(pot))

    def _deal_board_cards(self, street:Street, board:Board, deck:Deck) -> None:
        cards = []
        for _ in range(street.length):
            cards.append(deck.pop())
        board.append(*cards)

    def _deal_pocket_cards(self, street:Street, players:List[Player], deck:Deck) -> None:
        for player in self._get_active_players(players):
            cards = []
            for _ in range(street.length):
                cards.append(deck.pop())
            player.pocket.append(*cards)

    def _is_board_street(self, street:Street, board:Board) -> bool:
        return street in board.street_classes

    def _get_active_players(self, players:List[Player]) -> list:
        return [ x for x in players if x.is_active ]

    def _define_start_idx(self, street:Street, players:List[Player]) -> int:
        return 0


__all__ = ('Dealer',)
