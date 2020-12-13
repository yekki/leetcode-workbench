from common import Problem


class Solution(Problem):
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        for x in range(1, N + 1):
            s = str(x)
            ans += (all(d not in '347' for d in s) and any(d in '2569' for d in s))

        return ans

    def _validate(self, input, expected) -> tuple:
        result = self.rotatedDigits(input)

        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)