from typing import *


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		for idx, num in enumerate(nums):
			if num >= target:
				return idx

		return len(nums)
