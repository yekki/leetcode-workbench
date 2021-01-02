from common import Problem


class Solution(Problem):
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == "__main__":
    Solution.test(__file__)