from domain.support.base import Game, Pot


class Runner:
    @classmethod
    def run(cls, game: Game, attempts: int = 1) -> iter:
        for _ in range(attempts):
            yield cls._run_attempt(game=game)

    @classmethod
    def _run_attempt(cls, game: Game) -> Pot:
        return game.clone().run()
