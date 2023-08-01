from typing import *


class Solution:
	def alternatingSubarray(self, nums: List[int]) -> int:
		res = 0
		count = 1
		prev = nums[0]
		for i in range(1, len(nums)):
			if count % 2 == 1 and nums[i] == prev + 1:
				count += 1
			elif count % 2 == 0 and nums[i] == prev - 1:
				count += 1
			else:
				res = max(res, count)
				if nums[i] == prev + 1:
					count = 2
				else:
					count = 1
			prev = nums[i]
		res = max(res, count)
		return -1 if res < 2 else res


"""
s1 = s0 + 1
s2 = s1 - 1 = s0 + 1 - 1 = s0
s3 = s2 + 1 = s0 + 1
s4 = s3 - 1 = s0 + 1 - 1 = s0
"""
