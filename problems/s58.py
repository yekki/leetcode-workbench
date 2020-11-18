from . import AbstractSolution


class Solution(AbstractSolution):
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip.split(' ')

        return len(words[len(words) - 1])

    def _validate(self, input, expected) -> bool:
        result = self.lengthOfLastWord(input)

        return result == expected