from common import Problem


class Solution(Problem):
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry, ret = tmp // 10, str(tmp % 10) + ret
            i, j = i - 1, j - 1

        return '1' + ret if carry else ret


if __name__ == '__main__':
    Solution.test(__file__)