from common import Problem


class Solution(Problem):

    def _validate(self, input, expected) -> tuple:
        result = self

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)