class Suit():
    """
    Representation of abstract suit
    """

    def __init__(self, code:str, name:str, order:int, weight:int) -> None:
        assert len(code) == 1 and 'a' <= code <= 'z', 'Code must be a single lowercase char from a to z'
        assert len(name) > 0, 'Name must be specified'
        assert order > 0, 'Order must be a positive int'
        assert weight > 0, 'Weight must be a positive int'

        self._code = code
        self._name = name
        self._order = order
        self._weight = weight

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

    def __gt__(self, other:'Suit') -> bool:
        return self._order > other._order

    def __ge__(self, other:'Suit') -> bool:
        return self._order >= other._order

    def __lt__(self, other:'Suit') -> bool:
        return self._order < other._order

    def __le__(self, other:'Suit') -> bool:
        return self._order <= other._order

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def order(self):
        return self._order

    @property
    def weight(self):
        return self._weight
