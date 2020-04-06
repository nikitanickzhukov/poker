from abc import ABC
from functools import total_ordering

from utils.attrs import Attr


@total_ordering
class Prop(ABC):
    """
    An abstract card property

    Parameters
    ----------
        The same as attributes

    Attributes
    ----------
        code : str
            A code name (single char, read only)
        name : str
            A full name (read only)
        weight : int
            A weight for comparing with other instances (> 0, read only)

    Methods
    -------
        __str__()
        __repr__()
        __hash__()
        Comparing operations
    """

    code = Attr()
    name = Attr()
    weight = Attr()

    def __init__(self, code:str, name:str, weight:int) -> None:
        assert isinstance(code, str) and len(code) == 1, '`code` must be a single char'
        assert isinstance(name, str) and len(name) > 0, '`name` must be specified'
        assert isinstance(weight, int) and weight > 0, '`weight` must be a positive integer'

        self._code = code
        self._name = name
        self._weight = weight

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._name)

    def __hash__(self) -> int:
        return hash(self._code)

    def __eq__(self, other:'Prop') -> bool:
        if self.__class__ != other.__class__:
            raise TypeError()
        return self._code == other._code

    def __gt__(self, other:'Prop') -> bool:
        if self.__class__ != other.__class__:
            raise TypeError()
        return self._weight > other._weight


__all__ = ('Prop',)
