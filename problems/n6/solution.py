from common import Problem


class Solution(Problem):
    def convert(self, s: str, numRows: int) -> str:
        pass
    
    def _validate(self, input, expected) -> tuple:
        result = self.convert(input['p1'], input['p2'])

        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)