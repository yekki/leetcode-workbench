from common import Problem
import math


class Solution(Problem):
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def _validate(self, input, expected) -> bool:
        result = self.mySqrt(input)

        return expected == result


if __name__ == '__main__':
    Solution.test(__file__)