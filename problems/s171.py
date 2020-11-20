from . import AbstractSolution


class Solution(AbstractSolution):
    def titleToNumber(self, s: str) -> int:

        num = 0
        for c in s:
            num = num * 26 + ord(c) - ord("A") + 1

        return num

    def _validate(self, input, expected) -> bool:
        result = self.titleToNumber(input)

        return result == expected