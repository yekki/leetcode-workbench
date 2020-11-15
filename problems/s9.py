from common import AbstractSolution


class Solution(AbstractSolution):
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0:
            return False

        return x == int(str(x)[::-1])

    def _validate(self, input, expected) ->bool:
        return expected == self.isPalindrome(input)