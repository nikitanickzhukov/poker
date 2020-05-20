from typing import Union
from functools import total_ordering


@total_ordering
class Chips:
    __slots__ = ('_amount',)

    def __init__(self, amount: int = 0) -> None:
        if amount < 0:
            raise ValueError('Cannot be negative')
        self._amount = amount

    def __repr__(self) -> str:
        return repr(self._amount) + ' chip(s)'

    def __str__(self) -> str:
        return str(self._amount)

    def __bool__(self) -> bool:
        return bool(self._amount)

    def __int__(self) -> int:
        return self._amount

    def __eq__(self, other: 'Chips') -> bool:
        if issubclass(other.__class__, self.__class__):
            return self._amount == other._amount
        return NotImplemented

    def __gt__(self, other: 'Chips') -> bool:
        if issubclass(other.__class__, self.__class__):
            return self._amount > other._amount
        return NotImplemented

    def __add__(self, other: 'Chips') -> 'Chips':
        if isinstance(other, self.__class__):
            return self.__class__(self._amount + other._amount)
        return NotImplemented

    def __sub__(self, other: 'Chips') -> 'Chips':
        if isinstance(other, self.__class__):
            return self.__class__(self._amount - other._amount)
        return NotImplemented

    def __mul__(self, other: int) -> 'Chips':
        if isinstance(other, int):
            return self.__class__(self._amount * other)
        return NotImplemented

    def __rmul__(self, other: int) -> 'Chips':
        return self.__mul__(other)

    def __floordiv__(self, other: Union['Chips', int]) -> Union['Chips', int]:
        if isinstance(other, self.__class__):
            return self._amount // other._amount
        if isinstance(other, int):
            return self.__class__(self._amount // other)
        return NotImplemented

    def __truediv__(self, other: Union['Chips', int]) -> Union['Chips', float]:
        if isinstance(other, self.__class__):
            return self._amount / other._amount
        if isinstance(other, int):
            return self.__class__(self._amount // other)
        return NotImplemented

    def __mod__(self, other: Union['Chips', int]) -> Union['Chips', int]:
        if isinstance(other, self.__class__):
            return self._amount % other._amount
        if isinstance(other, int):
            return self.__class__(self._amount % other)
        return NotImplemented

    def __divmod__(self, other: Union['Chips', int]) -> tuple:
        if isinstance(other, self.__class__):
            return divmod(self._amount, other._amount)
        if isinstance(other, int):
            return self.__floordiv__(other), self.__mod__(other)
        return NotImplemented


__all__ = ('Chips',)
