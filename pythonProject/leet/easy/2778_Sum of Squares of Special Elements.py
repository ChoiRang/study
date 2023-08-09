from typing import *


class Solution:
	def sumOfSquares(self, nums: List[int]) -> int:
		n = len(nums)
		res = 0
		for i, num in enumerate(nums):
			if n % (i + 1) == 0:
				res += (num ** 2)
		return res
