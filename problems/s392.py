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

    def _validate(self, input, expected) -> bool:
        return expected == self.isSubsequence(input['p1'], input['p2'])


if __name__ == '__main__':
    Solution.test(__file__)