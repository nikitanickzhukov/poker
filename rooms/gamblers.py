class Gambler():
    __slots__ = ('_nickname',)

    def __init__(self, nickname:str) -> None:
        assert len(nickname) > 0, '{} nickname cannot be empty'.format(self.__class__.__name__)
        self._nickname = nickname

    def __repr__(self) -> str:
        return '<{}: {}>'.format(self.__class__.__name__, self._nickname)

    def __str__(self) -> str:
        return self._nickname

    def __hash__(self) -> int:
        return hash(self._nickname)


__all__ = ('Gambler',)
