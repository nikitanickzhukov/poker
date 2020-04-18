import time


class Timer():
    def __init__(self, func=time.perf_counter):
        self._func = func
        self._start = None
        self._elapsed = 0.0

    def start(self):
        if self.running:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if not self.running:
            raise RuntimeError('Not started')
        finish = self._func()
        self._elapsed += finish - self._start
        self._start = None

    def reset(self):
        if self.running:
            self.stop()
        self._elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    @property
    def elapsed(self):
        return self._elapsed

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


__all__ = ('Timer')
