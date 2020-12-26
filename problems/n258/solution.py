from common import Problem


class Solution(Problem):
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9

    def _validate(self, input, expected) -> tuple:
        result = self.addDigits(input)

        return expected == result, result


if __name__ == "__main__":
    Solution.test(__file__)