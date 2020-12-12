from common import Problem
from typing import List


class Solution(Problem):
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrace(index, path):
            res.append(path)
            if index >= len(nums):
                return

            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                backtrace(i + 1, path + [nums[i]])
                used[i] = False
            return

        res = []
        if not nums:
            return res
        nums.sort()
        used = [False] * len(nums)
        backtrace(0, [])

        return res

    def _validate(self, input, expected) -> tuple:
        result = self.subsetsWithDup(input)

        return result.sort() == expected.sort(), result


if __name__ == '__main__':
    Solution.test(__file__)