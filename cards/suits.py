from typing import List, Optional


class Suit():
    """
    Representation of abstract suit
    """

    def __init__(self, code:str, name:str) -> None:
        assert len(code) == 1 and 'a' <= code <= 'z', 'Code must be a single lowercase char from a to z'
        assert len(name) > 0, 'Name must be specified'

        self._code = code
        self._name = name

    def __repr__(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return ord(self._code)

    def __str__(self) -> str:
        return self._name

    def __eq__(self, other:'Suit') -> bool:
        return self._code == other._code

    def __ne__(self, other:'Suit') -> bool:
        return self._code != other._code

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name


class SuitSet():
    """
    Representation of abstract set of suits
    """

    def __init__(self, items:List[Suit]):
        self._items = set(items)

    def __repr__(self) -> str:
        return repr(self._items)

    def __str__(self) -> str:
        return str(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __eq__(self, other:'SuitSet') -> bool:
        return self._items == other._items

    def __ne__(self, other:'SuitSet') -> bool:
        return self._items != other._items

    def __contains__(self, item:Suit) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> iter:
        return iter(self._items)

    def __getitem__(self, key:str) -> Suit:
        for x in self._items:
            if x.code == key:
                return x
        raise KeyError('Suit %s is not found' % (key,))


spades:Suit = Suit('s', 'spades')
hearts:Suit = Suit('h', 'hearts')
diamonds:Suit = Suit('d', 'diamonds')
clubs:Suit = Suit('c', 'clubs')

standard_suits:SuitSet = SuitSet([ spades, hearts, diamonds, clubs, ])
