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
            return None

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, num in enumerate(nums):
            gap = target - nums[i]
            if gap in hashmap:
                return [i, hashmap.get(gap)]
            hashmap[num] = i
        else:
            return None

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        else:
            return None

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) -1

        while i < j:
            sum = nums[i] + nums[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i, j]
        else:
            return None

    def prepare_test(self):
        self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__, 1)