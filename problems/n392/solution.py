from common import Problem
import collections


class Solution(Problem):
    def isSubsequence(self, s: str, t: str) -> bool:
        queue = collections.deque(s)
        for c in t:
            if not queue:
                return True
            if c == queue[0]:
                queue.popleft()
        return not queue


if __name__ == '__main__':
    Solution.test(__file__)