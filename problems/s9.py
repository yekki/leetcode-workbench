from common import AbstractSolution


class Solution(AbstractSolution):

    def _validate(self, input, expected):
        return expected == self.isPalindrome(input)

    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0:
            return False

        return x == int(str(x)[::-1])


if __name__ == '__main__':
    s = Solution('/samples/9.json')
    print(s.validate())