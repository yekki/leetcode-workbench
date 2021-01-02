from common import Problem, list_eq
from typing import List


class Solution(Problem):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            gap = target - nums[i]
            j = i + 1
            if gap in nums[j:]:
                return [i, nums[j:].index(gap) + i + 1]
        else:
            return []

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, num in enumerate(nums):
            gap = target - nums[i]
            if gap in hashmap:
                return [i, hashmap.get(gap)]
            hashmap[num] = i
        else:
            return []

    def eq(self, result, expected):
        return list_eq(result, expected)


if __name__ == '__main__':
    Solution.test(__file__)