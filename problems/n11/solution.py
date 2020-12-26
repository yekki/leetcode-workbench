from common import Problem
from typing import List


class Solution(Problem):
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

    def _validate(self, input, expected) -> tuple:
        result = self.maxArea(input)

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)