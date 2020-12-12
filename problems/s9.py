from common import Problem


class Solution(Problem):
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0:
            return False

        return x == int(str(x)[::-1])

    def _validate(self, input, expected) -> tuple:
        result = self.isPalindrome(input)

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)