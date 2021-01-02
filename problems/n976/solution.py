from common import Problem
from typing import List


class Solution(Problem):
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        else:
            return 0


if __name__ == '__main__':
    Solution.test(__file__)
