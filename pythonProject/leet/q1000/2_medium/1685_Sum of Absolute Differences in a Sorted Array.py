from typing import *


class Solution:
	def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
		total = sum(nums)
		pre = 0
		n = len(nums)
		res = []
		for i in range(n):
			res.append((2 * i - n) * nums[i] + total - pre)
			total -= nums[i]
			pre += nums[i]

		return res
