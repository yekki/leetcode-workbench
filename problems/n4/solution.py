from common import Problem
from typing import List
import statistics

class Solution(Problem):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        return statistics.median(nums1)

    def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        c = len(nums1)
        nums1.sort()
        if c % 2 != 0:
            return nums1[c//2]
        else:
            return (nums1[c//2] + nums1[(c - 1)//2]) / 2


if __name__ == '__main__':
    Solution.test(__file__)