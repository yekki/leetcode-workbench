from typing import List


INPUT = ([2, 7, 11, 15], 9)
EXPECTED = [0, 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in nums[i + 1:]:
                return [i, nums[i + 1:].index(gap) + i + 1]
        return None
