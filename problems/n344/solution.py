from common import Problem, list_eq
from typing import List


class Solution(Problem):
    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def post_case(self, case):
        case['actual'] = case['params']

    # def prepare_test(self):
    #     self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__)