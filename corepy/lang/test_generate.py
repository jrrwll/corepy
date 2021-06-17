from unittest import TestCase

from corepy.internal.generate import generate_init


class generate_test(TestCase):
    def test_PID_S(self):
        generate_init("username, password, timeout, endpoint")
