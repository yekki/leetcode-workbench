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
            l = 0
            for i in range(1, len(s)):
                if s[i].isdecimal():
                    l = i + 1
                else:
                    print("fuck")
                    n = int(s) * flag
                    if n < -2 ** 31:
                        return -2 ** 31
                    if n >= 2 ** 31:
                        return 2 ** 31 - 1

                    return n
            else:
                s = s[0:l]
                n = int(s) * flag
                return n
        return 0


if __name__ == '__main__':
    Solution.test(__file__)