from common import Problem
from typing import List
import itertools


class Solution(Problem):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        for i in range(len(nums) +1):
            for j in itertools.combinations(nums, i):
                ret.append(j)

        return ret

    #TODO
    def _validate(self, input, expected) -> bool:
        result = None

        return result == expected


if __name__ == '__main__':
    Solution.test(__file__)