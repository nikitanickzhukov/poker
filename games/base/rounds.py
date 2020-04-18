from typing import List, Optional
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
    pocket_class = None
    hand_class = None

    players = ListAttr(
        type=tuple,
        item_type=Player,
        writable=False,
        validate=lambda obj, val: len(set(map(lambda x: len(x.pocket or []), val))) == 1
    )
    bb = IntegerAttr(min_value=0, writable=False)
    sb = IntegerAttr(min_value=0, writable=False)
    ante = IntegerAttr(min_value=0, writable=False)
    deck = TypedAttr(type=Deck, writable=False)
    board = TypedAttr(type=Board, writable=False)
    street_classes = ListAttr(
        type=tuple,
        item_type=Street,
        getter=lambda obj: sorted(obj.pocket_class.street_classes + obj.board_class.street_classes, key=lambda x: x.order),
    )

    def __init__(self, players:List[Player], bb:int, sb:int, ante:int=0, board:Optional[Board]=None) -> None:
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

        if board is None:
            board = self.board_class()
        self.__class__.board.validate(self, board)
        self._board = board

        for player in self._players:
            if player.pocket is None:
                player.pocket = self.pocket_class()

    def start(self) -> None:
        idx = self._get_street_idx()
        while idx < len(self.street_classes):
            street = self.street_classes[idx]
            self._run_street(street)
            idx = self._get_street_idx()
        self._showdown()

    def _get_street_idx(self) -> int:
        idx = 0
        for i, street_class in enumerate(self.street_classes):
            if street_class in self.board_class.street_classes:
                for street in self.board.streets:
                    if isinstance(street, street_class):
                        idx = i + 1
            else:
                for street in self.players[0].pocket.streets:
                    if isinstance(street, street_class):
                        idx = i + 1
        return idx

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
        for player in self._players:
            hand = self.hand_class.identify(player.pocket, self._board)
            print(repr(player), ' == ', repr(hand))

    def _is_board_street(self, street:Street) -> bool:
        return street in self.board_class.street_classes


__all__ = ('Round',)
