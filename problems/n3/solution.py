from common import Problem


class Solution(Problem):
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        tmp = ''

        for c in s:
            if c not in tmp:
                tmp += c
            else:
                tmp = tmp[tmp.index(c) + 1:]
                tmp += c

            if len(tmp) > len(ans):
                ans = tmp

        return len(ans)


if __name__ == '__main__':
    Solution.test(__file__)