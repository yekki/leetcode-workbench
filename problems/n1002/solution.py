from common import Problem, list_eq
from typing import List
import collections


class Solution(Problem):
    def commonChars(self, A: List[str]) -> List[str]:
        c = collections.Counter(A[0])

        for a in A:
            c &= collections.Counter(a)

        return c.elements()

    @staticmethod
    def eq(result, expected):
        list_eq(result, expected)

    #TODO error
    def _validate(self, input, expected) -> tuple:
        result = self.commonChars(input)

        return list_eq(result, expected), result


if __name__ == '__main__':
    Solution.test(__file__)