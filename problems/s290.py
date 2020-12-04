from common import Problem


class Solution(Problem):

    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split()
        return list(map(pattern.index, pattern)) == list(map(res.index, res))

    def _validate(self, input, expected) -> bool:
        result = self.wordPattern(input['p1'], input['p2'])

        return result == expected


if __name__ == '__main__':
    Solution.test(__file__)