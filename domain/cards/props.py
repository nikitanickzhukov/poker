from abc import ABC
from functools import total_ordering


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
            A weight for comparing with other instances (positive, read only)

    Methods
    -------
        __str__()
        __repr__()
        __hash__()
        Comparing operations
    """

    __slots__ = ('_code', '_name', '_weight')

    def __init__(self, code: str, name: str, weight: int) -> None:
        assert len(code) == 1, '{} code must be a single char'.format(self.__class__.__name__)
        assert len(name) > 0, '{} name must not be empty'.format(self.__class__.__name__)
        assert weight > 0, '{} weight must be positive'.format(self.__class__.__name__)

        self._code = code
        self._name = name
        self._weight = weight

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._name)

    def __hash__(self) -> int:
        return hash(self._code)

    def __eq__(self, other: 'Prop') -> bool:
        if self.__class__ != other.__class__:
            raise TypeError()
        return self._weight == other._weight

    def __gt__(self, other: 'Prop') -> bool:
        if self.__class__ != other.__class__:
            raise TypeError()
        return self._weight > other._weight

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight


__all__ = ('Prop',)
