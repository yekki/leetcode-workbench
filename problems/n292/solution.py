from common import Problem


class Solution(Problem):
    def canWinNim(self, n: int) -> bool:
        return bool(n % 4)

    def _validate(self, input, expected) -> tuple:
        result = self.canWinNim(input)
        return result == expected, result


if __name__ == "__main__":
    Solution.test(__file__)
