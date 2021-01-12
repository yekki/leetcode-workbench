from common import Problem
from typing import List


def eq(result, expected):
    return result.sort() == expected.sort()

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

    def prepare_test(self):
        self.eq = eq


if __name__ == '__main__':
    Solution.test(__file__)