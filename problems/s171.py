from common import Problem, test


class Solution(Problem):
    def titleToNumber(self, s: str) -> int:

        num = 0
        for c in s:
            num = num * 26 + ord(c) - ord("A") + 1

        return num

    def _validate(self, input, expected) -> bool:
        result = self.titleToNumber(input)

        return result == expected


if __name__ == '__main__':
    Solution.test(__file__)

