from common import Problem


class Solution(Problem):
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = 0
        s2 = 0
        for c in s:
            s1 += ord(c)

        for c in t:
            s2 += ord(c)

        return chr(s2 - s1)

    def _validate(self, input, expected) -> bool:
        result = self.findTheDifference(input['p1'], input['p2'])

        return result == expected


if __name__ == '__main__':
    Solution.test(__file__)