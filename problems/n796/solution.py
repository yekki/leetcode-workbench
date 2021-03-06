from common import Problem
from collections import deque


class Solution(Problem):
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True

        s = deque(A)
        for i in range(len(A) -1):
            s.append(s.popleft())
            if s == deque(B):
                return True
        else:
            return False


if __name__ == '__main__':
    Solution.test(__file__, 1)