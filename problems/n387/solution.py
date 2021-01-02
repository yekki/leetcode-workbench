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


if __name__ == '__main__':
    Solution.test(__file__)