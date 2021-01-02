from common import Problem, list_eq
from typing import List


class Solution(Problem):
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        pairs = []

        for i in range(len(nums)):
            pairs.append([i, nums[i]])

        pairs.sort(key=lambda p: p[1], reverse=True)

        for i in range(len(nums)):
            if i == 0:
                nums[pairs[i][0]] = 'Gold Medal'

            elif i == 1:
                nums[pairs[i][0]] = 'Silver Medal'
            elif i == 2:
                nums[pairs[i][0]] = 'Bronze Medal'
            else:
                nums[pairs[i][0]] = str(i + 1)

        return nums



if __name__ == '__main__':
    Solution.test(__file__)