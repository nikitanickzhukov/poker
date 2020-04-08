from utils.attrs import StringAttr
from .props import Prop


class Rank(Prop):
    """
    A card rank (see Prop docs for more information)
    """

    code = StringAttr(
        min_length=1,
        max_length=1,
        validate=lambda obj, val: 'A' <= val <= 'Z' or '0' <= val <= '9',
        writable=False,
    )


ranks = (
    Rank(code='A', name='Ace', weight=14),
    Rank(code='2', name='Deuce', weight=2),
    Rank(code='3', name='Trey', weight=3),
    Rank(code='4', name='Four', weight=4),
    Rank(code='5', name='Five', weight=5),
    Rank(code='6', name='Six', weight=6),
    Rank(code='7', name='Seven', weight=7),
    Rank(code='8', name='Eight', weight=8),
    Rank(code='9', name='Nine', weight=9),
    Rank(code='T', name='Ten', weight=10),
    Rank(code='J', name='Jack', weight=11),
    Rank(code='Q', name='Queen', weight=12),
    Rank(code='K', name='King', weight=13),
)


__all__ = ('Rank', 'ranks')
