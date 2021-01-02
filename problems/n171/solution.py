from common import Problem


class Solution(Problem):
    def titleToNumber(self, s: str) -> int:

        num = 0
        for c in s:
            num = num * 26 + ord(c) - ord("A") + 1

        return num


if __name__ == '__main__':
    Solution.test(__file__)

