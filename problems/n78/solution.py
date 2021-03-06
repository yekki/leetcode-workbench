from common import Problem, list_eq
from typing import List
import itertools


class Solution(Problem):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        for i in range(len(nums) +1):
            for j in itertools.combinations(nums, i):
                ret.append(list(j))

        return ret

    def prepare_test(self):
        self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__)