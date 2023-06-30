from typing import *


class Solution:
	def findNonMinOrMax(self, nums: List[int]) -> int:
		min_val, max_val = min(nums), max(nums)
		for num in nums:
			if num != min_val and num != max_val:
				return num
		return -1
