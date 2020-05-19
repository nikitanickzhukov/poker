from unittest import TestCase
import time

from engine.infrastructure.timer import Timer


class TimerTestCase(TestCase):
    def setUp(self):
        self.timer = Timer()
        self.delay = 1
        self.eps = 0.025

    def tearDown(self):
        del self.timer

    def test_timer(self):
        self.timer.start()
        time.sleep(self.delay)
        self.timer.stop()
        self.assertTrue(self.delay - self.eps <= self.timer.elapsed <= self.delay + self.eps)

        self.timer.reset()
        self.assertEqual(self.timer.elapsed, 0.0)

        with self.timer:
            time.sleep(1)
        self.assertTrue(self.delay - self.eps <= self.timer.elapsed <= self.delay + self.eps)
