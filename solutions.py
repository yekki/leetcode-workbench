import unittest
from common import timer
from n001.solution import Solution as S1, INPUT as I1, EXPECTED as E1
from n002.solution import Solution as S2, INPUT as I2, EXPECTED as E2
from n007.solution import Solution as S7, INPUT as I7, EXPECTED as E7
from n830.solution import Solution as S830, INPUT as I830, EXPECTED as E830

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

    @timer
    def test_7(self):
        s = S7()
        result = s.reverse(I7)
        self.assertEqual(result, E7)
    
    @timer
    def test_830(self):
        s = S830()
        result = s.largeGroupPositions(I830)
        print(result)
        self.assertTrue(E830, result)