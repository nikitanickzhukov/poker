from unittest import TestCase
import time

from utils.timer import Timer


class TimerTestCase(TestCase):
    def setUp(self):
        self.timer = Timer()

    def tearDown(self):
        del self.timer

    def test_timer(self):
        self.timer.start()
        time.sleep(1)
        self.timer.stop()
        self.assertTrue(0.95 <= self.timer.elapsed <= 1.05)

        self.timer.reset()
        self.assertEqual(self.timer.elapsed, 0.0)

        with self.timer:
            time.sleep(1)
        self.assertTrue(0.95 <= self.timer.elapsed <= 1.05)
