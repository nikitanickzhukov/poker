from domain.generic.cards import Deck

from .events import History
from .boards import Board
from .tables import Table
from .dealers import Dealer
from .pots import Pot


class Game:
    __slots__ = ('_history', '_deck', '_board', '_table', '_dealer', '_pot', '_identifier')
    street_classes = None
    identifier_class = None
    board_class = Board
    table_class = Table
    dealer_class = Dealer
    pot_class = Pot

    def __init__(self, history: History, deck: Deck) -> None:
        self._history = history
        self._deck = deck

        self._board = self.board_class()
        self._table = self.table_class()
        self._dealer = self.dealer_class()
        self._pot = self.pot_class()
        self._identifier = self.identifier_class()

    def run(self) -> None:
        self.prepare()
        self.start()
        self.finish()

    def prepare(self) -> None:
        self._dealer.restore_state(
            history=self._history,
            table=self._table,
            board=self._board,
            pot=self._pot,
        )
        self._dealer.shuffle_deck(deck=self._deck)

    def start(self) -> None:
        self._dealer.process(
            street_classes=self.street_classes,
            history=self._history,
            deck=self._deck,
            table=self._table,
            board=self._board,
            pot=self._pot,
        )

    def finish(self) -> None:
        self._dealer.showdown(
            table=self._table,
            board=self._board,
            pot=self._pot,
            identifier=self._identifier,
        )


__all__ = ('Game',)
