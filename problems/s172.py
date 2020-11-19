from . import AbstractSolution


class Solution(AbstractSolution):
    def trailingZeroes(self, n: int) -> int:
        result = 1

        while n > 1:
            result = result * n
            n -= 1

        s = str(result)
        n1 = len(s)
        n2 = len(str(int(s[::-1])))

        return n1 - n2

    def _validate(self, input, expected) -> bool:
        result = self.trailingZeroes(input)

        return expected == result