from common import Problem


class Solution(Problem):
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        ret = int(str(x)[::-1]) if x >0 else - int(str(-x)[::-1])
        return ret if pow(-2, 31) <= ret <= pow(2, 31) - 1 else 0


if __name__ == '__main__':
    Solution.test(__file__)