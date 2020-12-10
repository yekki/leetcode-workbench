from common import Problem
from typing import List

class Solution(Problem):
    def minDeletionSize(self, A: List[str]) -> int:
        for i in range(len(A) - 1):
            for j in range(len(A[0]) - 1):
                A

    def _validate(self, input, expected) -> bool:
        result = None

        return result == expected


if __name__ == '__main__':
    Solution.test(__file__)