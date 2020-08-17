from unittest import TestCase


class TestSomething(TestCase):

    def setUp(self):
        self.something = 1

    def test_one(self):
        self.assertEqual(self.something, 1)
