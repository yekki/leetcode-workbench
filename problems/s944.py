from common import Problem
from typing import List


class Solution(Problem):
    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i + 1] for i in range(len(col) - 1)):
                ans += 1
        return ans

    def _validate(self, input, expected) -> bool:

        return expected == self.minDeletionSize(input)


if __name__ == '__main__':
    Solution.test(__file__, 1)