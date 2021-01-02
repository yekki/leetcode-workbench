from common import Problem


class Solution(Problem):
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.replace('-', '').upper()
        n = len(s) // K
        l = len(s) % K

        if l == 0:
            r = s[0:K]
            n -= 1
            start = K
        else:
            r = s[0:l]
            start = l

        for i in range(n):
            r += '-'
            r += s[start:start + K]
            start += (start + K - 1)

        return r


if __name__ == '__main__':
    Solution.test(__file__)