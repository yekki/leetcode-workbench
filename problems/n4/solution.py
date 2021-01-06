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

    def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = [0] * (len(nums1) + len(nums2))
        i, l, r = 0, 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                nums3[i] = nums1[l]
                l += 1
            else:
                nums3[i] = nums2[r]
                r += 1
            i += 1

        if i == len(nums1):
            nums3[i:] = nums2[r:]
        else:
            nums3[i:] = nums2[l:]

        c = len(nums3)

        if c % 2 != 0:
            return float(nums1[c//2])
        else:
            return (nums1[c//2] + nums1[(c - 1)//2]) / 2


if __name__ == '__main__':
    Solution.test(__file__)