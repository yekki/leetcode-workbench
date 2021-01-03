from common import Problem
from typing import List


class Solution(Problem):
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def _validate(self, input, expected) -> tuple:
        self.reverseString(input)
        return input == expected, input


if __name__ == '__main__':
    Solution.test(__file__)