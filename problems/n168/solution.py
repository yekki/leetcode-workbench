from common import Problem


class Solution(Problem):
    def convertToTitle(self, n: int) -> str:
        l = []
        while (n > 0):
            if (n % 26 != 0):
                l.append(n % 26)
                n = n // 26
            else:
                n = n // 26
                l.append(26)
                n = n - 1
        s = ''
        for i in l[::-1]:
            s = s + chr(ord('A') + i - 1)
        return s

        return result

    def convertToTitle_1(self, n: int) -> str:
        l = []
        while (n > 0):
            if (n % 26 != 0):
                l.append(n % 26)
                n = n // 26
            else:
                n = n // 26
                l.append(26)
                n = n - 1
        s = ''
        for i in l[::-1]:
            s = s + chr(ord('A') + i - 1)
        return s

        return result


if __name__ == '__main__':
    Solution.test(__file__)