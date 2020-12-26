from common import Problem


class Solution(Problem):
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        while True:
            flag = num
            if not num % 2:
                num >>= 1
            if not num % 3:
                num //= 3
            if not num % 5:
                num //= 5
            if num == 1:
                return True
            if flag == num:
                return False

    def _validate(self, input, expected) -> tuple:
        result = self.isUgly(input)
        return expected == result, result


if __name__ == '__main__':
    Solution.test(__file__)