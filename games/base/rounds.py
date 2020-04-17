from typing import List
from abc import ABC

from utils.attrs import TypedAttr, IntegerAttr, ListAttr
from cards import Deck
from .streets import Street
from .boards import Board
from .players import Player
from .hands import HandIdentifier


class Round(ABC):
    deck_class = None
    board_class = None
    hand_class = None

    players = ListAttr(
        type=tuple,
        item_type=Player,
        writable=False
    )
    bb = IntegerAttr(min_value=0, writable=False)
    sb = IntegerAttr(min_value=0, writable=False)
    ante = IntegerAttr(min_value=0, writable=False)
    deck = TypedAttr(type=Deck, writable=False)
    board = TypedAttr(type=Board, writable=False)
    street_classes = ListAttr(
        type=tuple,
        item_type=Street,
        getter=lambda obj: sorted(obj._players[0].pocket_class.street_classes + obj.board_class.street_classes, key=lambda x: x.order),
    )
    street_idx = IntegerAttr(min_value=0, writable=False)

    def __init__(self, players:List[Player], bb:int, sb:int, ante:int=0) -> None:
        if not issubclass(self.hand_class, HandIdentifier):
            raise TypeError('`hand_class` must be a {} subclass'.format(HandIdentifier))

        self.__class__.players.validate(self, players)
        self.__class__.bb.validate(self, bb)
        self.__class__.sb.validate(self, sb)
        self.__class__.ante.validate(self, ante)

        self._players = players
        self._bb = bb
        self._sb = sb
        self._ante = ante

        deck = self.deck_class()
        self.__class__.deck.validate(self, deck)
        self._deck = deck
        self._deck.shuffle()

        board = self.board_class()
        self.__class__.board.validate(self, board)
        self._board = board

        self._street_idx = 0

    def start(self) -> None:
        while self._street_idx < len(self.street_classes):
            street = self.street_classes[self._street_idx]
            self._run_street(street)
            self._street_idx += 1

        self._showdown()

    def _run_street(self, street:Street) -> None:
        self._deal_cards(street)
        self._run_actions(street)

    def _deal_cards(self, street:Street) -> None:
        if self._is_board_street(street):
            self._deal_board_cards(street)
        else:
            self._deal_pocket_cards(street)

    def _deal_board_cards(self, street:Street) -> None:
        cards = []
        for _ in range(street.length):
            cards.append(self._deck.pop())
        self._board.append(*cards)

    def _deal_pocket_cards(self, street:Street) -> None:
        cards = [ [] for _ in range(len(self._players)) ]
        for _ in range(street.length):
            for card in cards:
                card.append(self._deck.pop())
        for player, card in zip(self._players, cards):
            player.append(*card)

    def _run_actions(self, street:Street) -> None:
        print(repr(street))
        print(repr(self._board))
        for player in self._players:
            print(repr(player))

    def _showdown(self) -> None:
        print('Showdown')
        print(repr(self._board))
        for player in self._players:
            hand = self.hand_class.identify(player.pocket, self._board)
            print(repr(player), ' == ', repr(hand))

    def _is_board_street(self, street:Street) -> bool:
        return street in self.board_class.street_classes


__all__ = ('Round',)
