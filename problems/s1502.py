from common import Problem
from typing import List

class Solution(Problem):
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        a = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
        if len(set(a)) == 1:
            return True
        else:
            return False

    def _validate(self, input, expected) -> tuple:
        result = self.canMakeArithmeticProgression(input)

        return result == expected, expected


if __name__ == '__main__':
    Solution.test(__file__)