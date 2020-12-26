from common import Problem
from typing import List


class Solution(Problem):
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)

        return max(c.keys(), key=c.get)

    def _validate(self, input, expected) -> tuple:
        result = self.majorityElement(input)
        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)