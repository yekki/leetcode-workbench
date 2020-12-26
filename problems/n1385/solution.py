from common import Problem
from typing import List

class Solution(Problem):
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in arr1:
            if all([abs((i - j)) > d for j in arr2]):
                ans += 1

        return ans

    def _validate(self, input, expected) -> tuple:
        result = self.findTheDistanceValue(input['p1'], input['p2'], input['p3'])

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__, 1)