from common import Problem


class Solution(Problem):
    def trailingZeroes(self, n: int) -> int:
        result = 1

        while n > 1:
            result = result * n
            n -= 1

        s = str(result)
        n1 = len(s)
        n2 = len(str(int(s[::-1])))

        return n1 - n2

    def _validate(self, input, expected) -> tuple:
        result = self.trailingZeroes(input)

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)