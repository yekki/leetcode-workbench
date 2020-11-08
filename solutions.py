import unittest
from common import timer
from n001.solution import Solution as S1, INPUT as I1, EXPECTED as E1
from n002.solution import Solution as S2, INPUT as I2, EXPECTED as E2


class SolutionTestCase(unittest.TestCase):

    @timer
    def test_1(self):
        import operator
        s = S1()
        result = s.twoSum(I1[0], I1[1])
        self.assertTrue(operator.eq(E1, result))

    @timer
    def test_2(self):
        s = S2()
        result = s.addTwoNumbers(I2[0], I2[1])
        self.assertTrue(result == E2)
