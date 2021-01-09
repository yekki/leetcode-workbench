from common import Problem
from typing import List
import statistics

class Solution(Problem):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        return statistics.median(nums1)

    def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        quotient, left = divmod(len(nums1), 2)

        if left == 0:
            median = (nums1[quotient - 1] + nums1[quotient]) / 2.0
        else:
            median = float(nums1[quotient])

        return median

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

        if l == len(nums1):
            nums3[i:] = nums2[r:]
        else:
            nums3[i:] = nums1[l:]

        quotient, left = divmod(len(nums3), 2)

        if left == 0:
            median = (nums3[quotient - 1] + nums3[quotient]) / 2.0
        else:
            median = float(nums3[quotient])

        return median


if __name__ == '__main__':
    Solution.test(__file__)