from common import Problem
from typing import List


class Solution(Problem):
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in arr1:
            if all([abs((i - j)) > d for j in arr2]):
                ans += 1

        return ans


if __name__ == '__main__':
    Solution.test(__file__)