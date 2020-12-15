from common import Problem


class Solution(Problem):
    def numberOfMatches(self, n: int) -> int:
        return n - 1

    def _validate(self, input, expected) -> tuple:
        result = self.numberOfMatches(input)

        return result == expected, expected


if __name__ == '__main__':
    Solution.test(__file__)