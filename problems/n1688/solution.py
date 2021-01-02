from common import Problem


class Solution(Problem):
    def numberOfMatches(self, n: int) -> int:
        return n - 1


if __name__ == '__main__':
    Solution.test(__file__)