class Rank():
    """
    Representation of abstract rank
    """

    def __init__(self, code:str, name:str, weight:int) -> None:
        assert len(code) == 1 and ('A' <= code <= 'Z' or '0' <= code <= '9'), \
               'Code must be a single uppercase char from A to Z or from 0 to 9'
        assert len(name) > 0, 'Name must be specified'
        assert weight > 0, 'Weight must be a positive int'

        self._code = code
        self._name = name
        self._weight = weight

    def __str__(self) -> str:
        return self._code

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._name)

    def __hash__(self) -> int:
        return hash(self._code)

    def __eq__(self, other:'Rank') -> bool:
        return self._code == other._code

    def __ne__(self, other:'Rank') -> bool:
        return self._code != other._code

    def __gt__(self, other:'Rank') -> bool:
        return self._weight > other._weight

    def __ge__(self, other:'Rank') -> bool:
        return self._weight >= other._weight

    def __lt__(self, other:'Rank') -> bool:
        return self._weight < other._weight

    def __le__(self, other:'Rank') -> bool:
        return self._weight <= other._weight

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight


__all__ = ('Rank',)
