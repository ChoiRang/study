from typing import *


class Solution:
	def maxArrayValue(self, nums: List[int]) -> int:
		n = len(nums)
		curr = 0
		for i in range(n - 1, -1, -1):
			if nums[i] > curr:
				curr = nums[i]
			else:
				curr += nums[i]

		return curr


"""
nums[i] <= nums[i+1] -> i+1 값이 항상 커야함 -> 역순으로 진행하면서 더하면 항상 큰값
"""
