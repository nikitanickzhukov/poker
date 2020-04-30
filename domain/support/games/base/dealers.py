from domain.generic.cards import Deck

from .actions import Fold, Check, Bet, Raise
from .streets import Street
from .boards import Board
from .layouts import Layout
from .pots import Pot
from .hands import Identifier


class Dealer():
    def shuffle_deck(self, deck:Deck) -> None:
        deck.shuffle()

    def deal_cards(
        self,
        street:Street,
        board:Board,
        layout:Layout,
        deck:Deck,
    ) -> None:
        if self._is_board_street(street=street, board=board):
            self._deal_board_cards(street=street, board=board, deck=deck)
            print(repr(board))
        else:
            self._deal_pocket_cards(street=street, layout=layout, deck=deck)
            for player in layout:
                print(repr(player))

    def collect_ante(self, layout:Layout, pot:Pot, ante:int) -> iter:
        for player in layout:
            action = player.post_ante(chips=ante)
            pot.add_chips(chips)
            yield action

    def collect_blinds(self, layout:Layout, pot:Pot, bb:int, sb:int, ante:int=0) -> iter:
        action = layout.sb_player.post_blind(chips=sb)
        pot.add_chips(action.chips)
        yield action

        action = layout.bb_player.post_blind(chips=bb)
        pot.add_chips(action.chips)
        yield action

        pot.bet = bb
        pot.step = bb
        pot.called = 1

    def request_actions(
        self,
        street:Street,
        board:Board,
        layout:Layout,
        pot:Pot,
    ) -> iter:
        print(repr(street))

        idx = self._define_start_idx(layout=layout, street=street)

        while pot.called != len(layout.active_players):
            player = layout.active_players[idx]

            action = player.do_action(board=board, street=street)

            print(player, repr(action))

            if isinstance(action, Fold):
                pot.remove_player(player)
            elif isinstance(action, Check):
                if pot.bet:
                    raise RuntimeError('Cannot check when there was a bet')
                pot.called += 1
            elif isinstance(action, Call):
                if not pot.bet:
                    raise RuntimeError('Cannot call when there was not a bet')
                pot.add_chips(action.chips)
                pot.called += 1
            elif isinstance(action, Bet):
                if action.chips - pot.bet < pot.step:
                    raise RuntimeError('Cannot bet less than step')
                pot.add_chips(action.chips)
                pot.step = action.chips - pot.bet
                pot.called = 1
                pot.bet = action.chips

            yield action

            if len(pot) == 1:
                break

            idx = idx + 1
            if idx == len(layout.active_players):
                idx = 0

        pot.reset()

    def showdown(self, layout:Layout, board:Board, pot:Pot, identifier:Identifier) -> None:
        print(repr(board))
        for player in layout.active_players:
            hand = identifier.identify(player.pocket, board)
            print(player, ' == ', repr(hand))
        print(repr(pot))

    def define_next_street(self, layout:Layout, board:Board) -> Street:
        street_classes = self._get_street_classes(layout=layout, board=board)
        idx = 0

        for i, street_class in enumerate(street_classes):
            if street_class in self._get_board_classes(board=board):
                for street in board.streets:
                    if isinstance(street, street_class):
                        idx = i + 1
            else:
                for street in layout[0].pocket.streets:
                    if isinstance(street, street_class):
                        idx = i + 1

        if idx < len(street_classes):
            return street_classes[idx]
        return None

    def _get_street_classes(self, layout:Layout, board:Board) -> tuple:
        classes = self._get_pocket_classes(layout=layout) + self._get_board_classes(board=board)
        return tuple(sorted(classes, key=lambda x: x.order))

    def _deal_board_cards(self, street:Street, board:Board, deck:'Deck') -> None:
        cards = []
        for _ in range(street.length):
            cards.append(deck.pop())
        board.append(*cards)

    def _deal_pocket_cards(self, street:Street, layout:Layout, deck:'Deck') -> None:
        deck.pop()
        for player in layout.active_players:
            cards = []
            for _ in range(street.length):
                cards.append(deck.pop())
            player.pocket.append(*cards)

    def _is_board_street(self, board:Board, street:Street) -> bool:
        return street in self._get_board_classes(board=board)

    def _define_start_idx(self, street:Street, layout:Layout) -> int:
        return 0

    def _get_board_classes(self, board:Board) -> tuple:
        return board.street_classes

    def _get_pocket_classes(self, layout:Layout) -> tuple:
        return layout.players[0].pocket.street_classes


__all__ = ('Dealer',)
