from common import Problem


class Solution(Problem):
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        s = s.rstrip()
        flag = 1

        if s[0] == '-':
            flag = -1
            s = s[1:]

        if s[0].isdecimal():
            l = 1
            for i in range(1, len(s)):
                if s[i].isdecimal():
                    l = i + 1
                else:
                    s = s[0:l]
                    break
        else:
            return 0

        n = int(s) * flag

        if n < -2 ** 31:
            return -2 ** 31
        if n >= 2 ** 31:
            return 2 ** 31 - 1

        return n


if __name__ == '__main__':
    Solution.test(__file__)