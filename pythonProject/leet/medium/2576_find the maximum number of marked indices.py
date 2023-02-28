from typing import *


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        nums.sort()
        left = nums[:N//2]
        right = nums[N//2:]

        while len(left) > 0 and len(right) > 0:
            if left[-1] * 2 <= right[-1]:
                result += 2
                left.pop()
                right.pop()
                continue
            left.pop()

        return result
