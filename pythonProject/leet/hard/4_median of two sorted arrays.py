from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        N = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[N-1] + nums[N]) / 2
        else:
            return float(nums[N])

        return 1.0
