from common import Problem
from typing import List


class Solution(Problem):
    def thirdMax(self, nums: List[int]) -> int:
        n = list(set(nums))
        n.sort(reverse=True)
        l = len(n)

        if l < 3:
            return n[0]
        else:
            return n[2]

    def _validate(self, input, expected) -> tuple:
        result = self.thirdMax(input)

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)