from common import Problem, list_eq
from typing import List


class Solution(Problem):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []

        if len(intervals) == 0:
            return res

        intervals.sort(key=lambda x: x[0])

        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])
        return res

    def prepare_test(self):
        self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__)