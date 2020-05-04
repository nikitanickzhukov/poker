from typing import List, Optional

from domain.generic.cards import Deck

from .streets import Street
from .boards import Board
from .layouts import Layout
from .pots import Pot
from .hands import Identifier
from .actions import Action
from .dealers import Dealer


class Game:
    __slots__ = ('_layout', '_dealer', '_board', '_pot', '_identifier', '_deck', '_bb', '_sb', '_ante', '_actions')

    def __init__(
        self,
        layout: Layout,
        dealer: Dealer,
        board: Board,
        pot: Pot,
        identifier: Identifier,
        deck: Deck,
        bb: int,
        sb: int,
        ante: int = 0,
        actions: Optional[List[Action]] = None,
    ) -> None:
        self._layout = layout
        self._dealer = dealer
        self._board = board
        self._deck = deck
        self._pot = pot
        self._identifier = identifier
        self._bb = bb
        self._sb = sb
        self._ante = ante
        self._actions = actions or []

    def run(self):
        self.prepare()
        self.start()
        self.finish()

    def prepare(self) -> None:
        self._dealer.shuffle_deck(deck=self._deck)

        """
        if self._ante:
            antes = self._dealer.collect_ante(
                layout=self._layout,
                pot=self._pot,
                ante=self._ante,
            )
            self._actions.extend(antes)
        blinds = self._dealer.collect_blinds(
            layout=self._layout,
            pot=self._pot,
            bb=self._bb,
            sb=self._sb,
        )
        self._actions.extend(blinds)
        """

    def start(self) -> None:
        street = self._dealer.define_next_street(
            layout=self._layout,
            board=self._board,
        )

        while street:
            self._dealer.deal_cards(
                street=street,
                layout=self._layout,
                board=self._board,
                deck=self._deck,
            )
            actions = self._dealer.request_actions(
                street=street,
                layout=self._layout,
                board=self._board,
                pot=self._pot,
            )
            self._actions.extend(actions)
            street = self._dealer.define_next_street(
                layout=self._layout,
                board=self._board,
            )

    def finish(self) -> None:
        self._dealer.showdown(
            layout=self._layout,
            board=self._board,
            pot=self._pot,
            identifier=self._identifier,
        )


__all__ = ('Game',)
