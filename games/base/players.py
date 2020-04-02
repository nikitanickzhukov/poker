class Player():
    nickname_length = 127

    def __init__(self, nickname:str) -> None:
        assert isinstance(nickname, str) and 1 <= len(nickname) <= self.nickname_length, \
               'Nickname must be a string from 1 to {} chars'.format(self.nickname_length)
        self._nickname = nickname

    def __repr__(self) -> str:
        return self.nickname

    def __str__(self) -> str:
        return self.nickname

    def __hash__(self) -> int:
        return hash(self.nickname)

    @property
    def nickname(self) -> str:
        return self._nickname


__all__ = ('Player',)
