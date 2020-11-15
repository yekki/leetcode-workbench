import unittest
from common import timer
from problems.n9 import Solution as S9


class SolutionTestCase(unittest.TestCase):

    @timer
    def test_9(self):
        self.assertTrue(S9().validate())


