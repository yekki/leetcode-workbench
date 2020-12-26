from common import Problem
from typing import List


class Solution(Problem):
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        res = cur = nums[0]
        c = len(nums)
        for i in range(1, c):
            if cur > 0:
                cur += nums[i]
            else:
                cur = nums[i]

            res = max(res, cur)
        return res

    def _validate(self, input, expected) -> tuple:
        result = self.maxSubArray(input)

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)