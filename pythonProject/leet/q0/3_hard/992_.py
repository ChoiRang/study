from typing import *
import collections


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        left = 0
        res = 0
        count = 0
        for right, num in enumerate(nums):
            print(count, right)
            counter[num] += 1
            if len(counter) > k:
                count = 0
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
            while counter[nums[left]] > 1:
                counter[nums[left]] -= 1
                left += 1
                count += 1
            if len(counter) == k:
                res += count+1

        return res