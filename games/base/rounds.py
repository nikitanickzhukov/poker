from typing import List
from abc import ABC

from cards import Deck
from tools import Box
from .pockets import Pocket
from .boards import Board
from .hands import HandIdentifier


class Round(ABC):
    deck_class = None
    pocket_class = None
    board_class = None
    identifier_class = None

    def __init__(self, boxes:List[Box], bb:int, sb:int, ante:int=0) -> None:
        assert issubclass(self.deck_class, Deck), 'Deck class must be a deck subclass'
        assert issubclass(self.pocket_class, Pocket), 'Pocket class must be a pocket subclass'
        assert issubclass(self.board_class, Board), 'Board class must be a board subclass'
        assert issubclass(self.identifier_class, HandIdentifier), 'Identifier class must be a hand identifier subclass'

        assert all(isinstance(x, Box) for x in boxes), 'Boxes cannot contain non-box items'
        assert isinstance(bb, int) and bb > 0, 'BB must be a positive integer'
        assert isinstance(sb, int) and 0 < sb <= bb, 'SB must be a positive integer less or equal to BB'
        assert isinstance(ante, int) and ante >= 0, 'Ante must be a zero or a positive integer'

        self._boxes = tuple(boxes)
        self._bb = bb
        self._sb = sb
        self._ante = ante
        self._deck = self.deck_class()
        self._deck.shuffle()
        self._pockets = tuple(self.pocket_class() for _ in range(len(self._boxes)))
        self._board = self.board_class()
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
            identifier = self.identifier_class(board=self._board, pocket=pocket)
            hand = identifier.identify()
            print('Pocket', i, ': ', pocket, ' == ', repr(hand))

    @property
    def boxes(self) -> tuple:
        return self._boxes

    @property
    def bb(self) -> int:
        return self._bb

    @property
    def sb(self) -> int:
        return self._sb

    @property
    def ante(self) -> int:
        return self._ante

    @property
    def street_classes(self) -> list:
        return sorted(
            [ x for x in self.pocket_class.street_classes + self.board_class.street_classes ],
            key=lambda x: x.order,
        )

    def _is_pocket_street(self, street) -> bool:
        return street in self.pocket_class.street_classes


__all__ = ('Round',)
