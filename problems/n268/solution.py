from common import Problem
from typing import List


class Solution(Problem):
    def missingNumber(self, nums: List[int]) -> int:
        nset = set(nums)
        c = len(nums) + 1
        for n in range(c):
            if n not in nset:
                return n

    def _validate(self, input, expected) -> tuple:
        result = self.missingNumber(input)
        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)