from common import AbstractSolution


class Solution(AbstractSolution):
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

    def _validate(self, input, expected) -> bool:
        result = self.strStr(input["p1"], input["p2"])

        return expected == result