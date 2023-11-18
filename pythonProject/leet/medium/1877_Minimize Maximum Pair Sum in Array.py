from typing import *


class Solution:
	def minPairSum(self, nums: List[int]) -> int:
		n = len(nums)
		nums.sort()
		res = 0

		for i in range(n // 2):
			res = max(res, nums[i] + nums[n - 1 - i])

		return res
