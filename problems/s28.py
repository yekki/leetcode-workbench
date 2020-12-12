from common import Problem


class Solution(Problem):
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

    def _validate(self, input, expected) -> tuple:
        result = self.strStr(input["p1"], input["p2"])

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)