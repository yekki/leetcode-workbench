from common import Problem


class Solution(Problem):
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 1:
            return True

        chs = []

        for c in s:
            if c.isdigit():
                chs.append(c)
            elif c.isalpha():
                chs.append(c.lower())

        ss = "".join(chs)

        return ss == ss[::-1]


if __name__ == '__main__':
    Solution.test(__file__)