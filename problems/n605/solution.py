from common import Problem
from typing import List


class Solution(Problem):
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tem_list = [0] + flowerbed + [0]
        num = len(tem_list)
        k = 0
        for i in range(1, num - 1):
            if tem_list[i] == 0 and tem_list[i - 1] == 0 and tem_list[i + 1] == 0:
                tem_list[i] = 1
                k += 1
        return k >= n  ##注意这里是大于等于而不是等于，看清题目


if __name__ == '__main__':
    Solution.test(__file__)
