from common import Problem


class Solution(Problem):
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s

        first_match = (len(s) > 0) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))

        return first_match and self.isMatch(s[1:], p[1:])

    def _validate(self, input, expected) -> tuple:
        result = self.isMatch(input['p1'], input['p2'])

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)
