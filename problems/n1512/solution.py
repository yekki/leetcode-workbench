from typing import List
from common import Problem

#TODO 不理解
class Solution(Problem):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        return sum((value - 1) * value // 2 for value in dic.values())


if __name__ == '__main__':
    Solution.test(__file__)