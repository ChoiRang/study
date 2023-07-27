from typing import *


class Solution:
	def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
		res, count = 0, 0

		for i in range(len(nums)):
			if nums[i] > threshold:
				count = 0
			elif count == 0 and nums[i] % 2 == 0:
				count = 1
			elif count > 0 and nums[i] % 2 != nums[i - 1] % 2:
				count += 1
			else:
				count = 1 if nums[i] % 2 == 0 else 0
			res = max(res, count)

		return res
