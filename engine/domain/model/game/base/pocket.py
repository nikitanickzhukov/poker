from typing import Sequence

from engine.domain.model.card import Card

from .kit import Kit


class Pocket(Kit):
    def draw_cards(self, in_cards: Sequence[Card], out_cards: Sequence[Card]) -> None:
        assert len(in_cards) == len(out_cards), 'Must draw equal cards amount'
        assert all([x in self.cards for x in out_cards]), 'All out cards must be in pocket'
        for i, out_card in enumerate(out_cards):
            for street in self._streets:
                if out_card in street:
                    street.draw_cards(in_cards=(in_cards[i],), out_cards=(out_card,))


__all__ = ('Pocket',)
