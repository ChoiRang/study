from typing import *


class Solution:
	def findValueOfPartition(self, nums: List[int]) -> int:
		nums.sort()
		min_val = 10 ** 9 + 1
		for i in range(len(nums) - 1):
			num = nums[i + 1] - nums[i]
			if min_val > num:
				min_val = num
		return min_val
