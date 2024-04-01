from typing import *


class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		if k <= 1:
			return 0
		left = 0
		total = 1
		res = 0
		for right, num in enumerate(nums):
			total *= num
			while total >= k:
				total /= nums[left]
				left += 1
			res += right - left + 1

		return res



