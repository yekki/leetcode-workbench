from common import Problem


class Solution(Problem):
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        ret = nums[0]

        for i in range(1, n):
            ret ^= nums[i]

        return ret

    def _validate(self, input, expected) -> bool:
        result = self.xorOperation(input['p1'], input['p2'])

        return result == expected, expected


if __name__ == '__main__':
    Solution.test(__file__)