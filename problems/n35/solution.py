from common import Problem
from typing import List


class Solution(Problem):
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i, n in enumerate(nums):
                if n > target:
                    return i
            else:
                return len(nums)


if __name__ == '__main__':
    Solution.test(__file__)