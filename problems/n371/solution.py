from common import Problem


class Solution(Problem):
    def getSum(self, a: int, b: int) -> int:
        return sum((a, b))

    def getSum_1(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF

        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)

    def _validate(self, input, expected) -> tuple:
        result = self.getSum_1(input['p1'], input['p2'])
        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)