from typing import *


# timeout(On^2)
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(1)
            for idx, num in enumerate(nums):
                if idx != i:
                    result[-1] *= num
        return result


# 238ms, 21mb
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        p = 1
        for i in range(0, len(nums)):
            result.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * p
            p = p * nums[i]

        return result
    