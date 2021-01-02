from common import Problem


class Solution(Problem):
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


if __name__ == '__main__':
    Solution.test(__file__)