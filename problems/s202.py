from common import Problem


class Solution(Problem):
    def isHappy(self, n: int) -> bool:
        res_table = set()
        while 1:
            n = [int(i) ** 2 for i in str(n)]
            n = sum(n)
            if n == 1:
                return True
            elif n in res_table:
                return False
            else:
                res_table.add(n)
    
    def _validate(self, input, expected) -> tuple:
        result = self.isHappy(input)

        return expected == result, result


if __name__ == "__main__":
    Solution.test(__file__)
