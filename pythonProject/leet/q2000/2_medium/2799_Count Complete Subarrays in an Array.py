from typing import *
import collections


class Solution:
	def countCompleteSubarrays(self, nums: List[int]) -> int:
		count = collections.Counter()
		max_count = len(set(nums))
		res, idx = 0, 0

		for num in nums:
			count[num] += 1
			while len(count) == max_count:
				count[nums[idx]] -= 1
				if count[nums[idx]] == 0:
					del count[nums[idx]]
				idx += 1
			res += idx

		return res

"""
nums = [5,5,5,5] -> 10가지, 순서(중복 같지만 다름) subarray
[5] idx=1
[, 5], [5, 5] idx=2
[, , 5], [, 5, 5], [5, 5, 5] idx=3
[, , , 5], [, , 5, 5], [, 5, 5, 5], [5,5 ,5 ,5] idx=4
"""