from typing import List
from abc import ABC

from utils.attrs import TypedAttr, IntegerAttr, ListAttr
from cards import Deck
from rooms import Box
from .streets import Street
from .pockets import Pocket
from .boards import Board
from .hands import HandIdentifier


class Round(ABC):
    deck_class = None
    pocket_class = None
    board_class = None
    hand_class = None

    boxes = ListAttr(
        type=tuple,
        item_type=Box,
        writable=False
    )
    bb = IntegerAttr(min_value=0, writable=False)
    sb = IntegerAttr(min_value=0, writable=False)
    ante = IntegerAttr(min_value=0, writable=False)
    deck = TypedAttr(type=Deck, writable=False)
    board = TypedAttr(type=Board, writable=False)
    pockets = ListAttr(
        type=tuple,
        item_type=Pocket,
        writable=False
    )
    street_classes = ListAttr(
        type=tuple,
        item_type=Street,
        getter=lambda obj: sorted(obj.pocket_class.street_classes + obj.board_class.street_classes, key=lambda x: x.order),
    )
    street_idx = IntegerAttr(min_value=0, writable=False)

    def __init__(self, boxes:List[Box], bb:int, sb:int, ante:int=0) -> None:
        if not issubclass(self.hand_class, HandIdentifier):
            raise TypeError('`hand_class` must be a {} subclass'.format(HandIdentifier))

        self.__class__.boxes.validate(self, boxes)
        self.__class__.bb.validate(self, bb)
        self.__class__.sb.validate(self, sb)
        self.__class__.ante.validate(self, ante)

        self._boxes = boxes
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

        pockets = tuple(self.pocket_class() for _ in range(len(self._boxes)))
        self.__class__.pockets.validate(self, pockets)
        self._pockets = pockets

        self._street_idx = 0

    def start(self) -> None:
        while self._street_idx < len(self.street_classes):
            street = self.street_classes[self._street_idx]
            self._run_street(street)
            self._street_idx += 1

        self._showdown()

    def _run_street(self, street):
        self._deal_cards(street)
        self._run_actions(street)

    def _deal_cards(self, street) -> None:
        if self._is_pocket_street(street):
            cards = [ [] for _ in range(len(self._pockets)) ]
            for _ in range(street.length):
                for card in cards:
                    card.append(self._deck.pop())
            for pocket, card in zip(self._pockets, cards):
                pocket.append(*card)
        else:
            cards = []
            for _ in range(street.length):
                cards.append(self._deck.pop())
            self._board.append(*cards)

    def _run_actions(self, street) -> None:
        print(street)
        print('Board: ', self._board)
        for i, pocket in enumerate(self._pockets):
            print('Pocket', i, ': ', pocket)

    def _showdown(self) -> None:
        print('Showdown')
        for i, pocket in enumerate(self._pockets):
            hand = self.hand_class.identify(pocket, self._board)
            print('Pocket', i, ': ', pocket, ' == ', repr(hand))

    @property
    def street_classes(self) -> list:
        return sorted(
            [ x for x in self.pocket_class.street_classes + self.board_class.street_classes ],
            key=lambda x: x.order,
        )

    def _is_pocket_street(self, street) -> bool:
        return street in self.pocket_class.street_classes


__all__ = ('Round',)
