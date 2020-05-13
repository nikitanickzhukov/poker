from .props import Prop


class Suit(Prop):
    """
    A card suit (see Prop docs for more information)
    """

    pass


suits = (
    Suit(code='s', name='spades', weight=4),
    Suit(code='h', name='hearts', weight=3),
    Suit(code='d', name='diamonds', weight=2),
    Suit(code='c', name='clubs', weight=1),
)


__all__ = ('Suit', 'suits')
