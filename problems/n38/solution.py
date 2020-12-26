from common import Problem


class Solution(Problem):
    def countAndSay(self, n: int) -> str:
        s = '1'
        import re
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

    def _validate(self, input, expected) -> tuple:
        result = self.countAndSay(input)

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)