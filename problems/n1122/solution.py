from common import Problem
from typing import List


class Solution(Problem):
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ret = []
        gap = [i for i in arr1 if i not in arr2]
        gap.sort()

        for i in arr2:
            for j in arr1:
                if i == j:
                    ret.append(j)
        else:
            ret = ret + gap

        return ret


if __name__ == '__main__':
    Solution.test(__file__)