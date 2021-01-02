from common import Problem


class Solution(Problem):
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    def longestPalindrome_1(self, s: str) -> str:
        length = len(s)
        dp = [[1] * length for _ in range(length)]
        left, right = 0, 0  # 长度为1时
        for i in range(1, length):
            for j in range(length - i):
                if s[j] == s[j + i] and dp[j + 1][j + i - 1]:
                    dp[j][j + i] = 1
                    left, right = j, j + i
                else:
                    dp[j][j + i] = 0
        return s[left: right + 1]


if __name__ == '__main__':
    Solution.test(__file__)

