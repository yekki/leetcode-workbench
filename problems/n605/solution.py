from common import Problem
from typing import List


class Solution(Problem):
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 1: continue
            if i > 0 and flowerbed[i - 1] == 1: continue
            if i + 1 < m and flowerbed[i + 1] == 1: continue
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        return False


if __name__ == '__main__':
    Solution.test(__file__)