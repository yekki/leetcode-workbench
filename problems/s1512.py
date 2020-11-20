from typing import List
from . import AbstractSolution


class Solution(AbstractSolution):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        return sum((value -1)*value // 2 for value in dic.values())

    def _validate(self, input, expected) -> bool:
        result = self.numIdenticalPairs(input)

        return result == expected