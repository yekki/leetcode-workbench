from . import AbstractSolution
from typing import List


class Solution(AbstractSolution):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in nums[i + 1:]:
                return [i, nums[i + 1:].index(gap) + i + 1]
        return None

    def _validate(self, input, expected) -> bool:
        nums = input['p1']
        target = input['p2']
        result = self.twoSum(nums, target)

        return result == expected


