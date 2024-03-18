from typing import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        save = {}
        total = 0
        res = 0
        for i, num in enumerate(nums):
            total += num if num == 1 else -1
            if total == 0:
                res = i + 1
            elif total in save:
                res = max(res, i-save[total])
            else:
                save[total] = i
        return res
