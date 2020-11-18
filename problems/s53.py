from . import AbstractSolution
from typing import List


class Solution(AbstractSolution):
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

    def _validate(self, input, expected) -> bool:
        result = self.maxSubArray(input)

        return result == expected
