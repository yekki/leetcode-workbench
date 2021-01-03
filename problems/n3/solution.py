from common import Problem


class Solution(Problem):
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ''
        tmp = ''

        for c in s:
            if c in tmp:
                tmp = tmp[tmp.index(c) + 1:]

            tmp += c

            if len(tmp) > len(ans):
                ans = tmp

        return len(ans)

    def lengthOfLongestSubstring_1(self, s: str) -> int:
        occ = set()
        n = len(s)
        right, str_len = 0, 0
        for left in range(n):
            while right < n and s[right] not in occ:
                occ.add(s[right])
                right += 1
            if len(occ) > str_len:
                str_len = len(occ)
            occ.remove(s[left])

        return str_len


if __name__ == '__main__':
    Solution.test(__file__, 3)