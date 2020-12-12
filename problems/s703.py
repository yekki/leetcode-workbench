from common import Problem, exec_template_methods
from typing import List
import heapq


class Solution(Problem):

    class KthLargest:
        def __init__(self, k: int, nums: List[int]):

            self.pool = nums
            self.size = len(self.pool)
            self.k = k
            heapq.heapify(self.pool)
            while self.size > k:
                heapq.heappop(self.pool)
                self.size -= 1

        def add(self, val: int) -> int:
            if self.size < self.k:
                heapq.heappush(self.pool, val)
                self.size += 1
            elif val > self.pool[0]:
                heapq.heapreplace(self.pool, val)

            return self.pool[0]

    def _validate(self, input, expected) -> tuple:
        inst = Solution.KthLargest(*input['p2'][0])
        result = exec_template_methods(inst, input['p1'], input['p2'])
        return result == expected, result


if __name__ == '__main__':
    Solution.test(__file__)