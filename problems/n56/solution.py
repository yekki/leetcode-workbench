from common import Problem, list_eq
from typing import List


##TODO list compare
class Solution(Problem):
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        nums = []

        lx = intervals.pop(0)

        for i in range(len(intervals)):
            ly = intervals[i]

            if lx[0] <= ly[0]:
                if lx[1] <= ly[1]:
                    lx[1] = ly[1]
            else:
                nums.append(lx)
                lx = intervals[i].copy()

        nums.append(lx)

        return nums

    def prepare_test(self):
        self.eq = list_eq


if __name__ == '__main__':
    Solution.test(__file__)