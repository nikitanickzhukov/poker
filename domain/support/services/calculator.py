from . import Runner


class Calculator:
    def __init__(self, runner: Runner) -> None:
        self._runner = runner
        self._player_chips = defaultdict(int)
        self._total_chips = 0

    def calculate(self, attempts: int = 1):
        for pot in self._runner.run(attempts):
            self._add_pot(pot=pot)
        return self._get_equity()

    def _add_pot(self, pot: Pot) -> None:
        self._total_chips += pot.chips
        chips = round(pot.chips / len(pot))
        for player in pot:
            self._player_chips[player] += chips

    def _get_equity(self) -> dict:
        return {x: self._player_chips[x] / self._total_chips for x in self._player_chips}
