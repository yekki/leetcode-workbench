from common import Problem


class Solution(Problem):
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight_1(self, n: int) -> int:
        res = 0

        while n:
            res += n & 1
            n >>= 1

        return res

    def hammingWeight_2(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


if __name__ == '__main__':
    Solution.test(__file__)
