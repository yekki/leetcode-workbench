from common import Problem
import collections


class Solution(Problem):
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        c = collections.Counter(s)
        for k, v in c.items():
            if v == 1:
                return s.index(k)
        else:
            return -1

    def _validate(self, input, expected) -> tuple:
        result = self.firstUniqChar(input)

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)