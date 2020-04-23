from typing import List, Optional
from abc import ABC

from cards import Deck, StandardDeck
from .dealers import Dealer
from .pots import Pot
from .boards import Board
from .players import Player
from .hands import HandIdentifier


class Round(ABC):
    __slots__ = ('_players', '_bb', '_sb', '_ante', '_board', '_pot', '_deck', '_dealer')
    deck_class = StandardDeck
    dealer_class = Dealer
    pot_class = Pot
    board_class = None
    pocket_class = None
    hand_class = None

    def __init__(self, players:List[Player], bb:int, sb:int, ante:int=0, board:Optional[Board]=None, pot:Optional[Pot]=None, deck:Optional[Deck]=None) -> None:
        self._players = players
        for player in self._players:
            if player.pocket is None:
                player.pocket = self.pocket_class()
        self._bb = bb
        self._sb = sb
        self._ante = ante

        if deck is None:
            deck = self.deck_class()
        self._deck = deck
        self._deck.shuffle()

        if board is None:
            board = self.board_class()
        self._board = board

        if pot is None:
            pot = self.pot_class(players=players, chips=0)
        self._pot = pot

        self._dealer = self.dealer_class()

    def start(self) -> None:
        self._dealer.shuffle_deck(self._deck)

        street_classes = self._get_street_classes()
        idx = self._get_street_idx()

        while idx < len(street_classes):
            street = street_classes[idx]
            self._dealer.deal_cards(
                street=street,
                board=self._board,
                players=self._players,
                deck=self._deck,
            )
            self._dealer.request_actions(
                street=street,
                board=self._board,
                players=self._players,
                pot=self._pot,
            )
            idx = self._get_street_idx()
        self._dealer.showdown(
            board=self._board,
            players=self._players,
            pot=self._pot,
            hand_class=self.hand_class,
        )

    def _get_street_classes(self) -> tuple:
        classes = self.pocket_class.street_classes + self.board_class.street_classes
        return tuple(sorted(classes, key=lambda x: x.order))

    def _get_street_idx(self) -> int:
        street_classes = self._get_street_classes()
        idx = 0

        for i, street_class in enumerate(street_classes):
            if street_class in self.board_class.street_classes:
                for street in self._board.streets:
                    if isinstance(street, street_class):
                        idx = i + 1
            else:
                for street in self._players[0].pocket.streets:
                    if isinstance(street, street_class):
                        idx = i + 1
        return idx


__all__ = ('Round',)
