from common import Problem, list_eq
from typing import List
import collections


class Solution(Problem):
    def commonChars(self, A: List[str]) -> List[str]:
        c = collections.Counter(A[0])

        for a in A:
            c &= collections.Counter(a)

        return c.elements()

    def prepare_test(self):
        self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__)