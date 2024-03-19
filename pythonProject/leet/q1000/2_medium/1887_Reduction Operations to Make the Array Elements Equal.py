from typing import *


class Solution:
	def reductionOperations(self, nums: List[int]) -> int:
		nums.sort(reverse=True)
		res = 0
		stack = 0
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]:
				res += 1 + stack
			stack += 1

		return res
