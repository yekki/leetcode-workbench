from common import Problem


class Solution(Problem):
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split()
        return list(map(pattern.index, pattern)) == list(map(res.index, res))


if __name__ == '__main__':
    Solution.test(__file__)