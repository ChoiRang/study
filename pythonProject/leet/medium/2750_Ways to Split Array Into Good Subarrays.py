from typing import *


class Solution:
	def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
		res, count = 0, 0
		mod = 10 ** 9 + 7
		for num in nums:
			if res > 0 and num == 0:
				count += 1
			elif res > 0 and num == 1:
				res *= (count + 1)
				count = 0
			elif num == 1:
				res = 1

		return res % mod
