from typing import *


class Solution:
	def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
		prev_count = -1
		res = 10 ** 9
		for divis in divisors:
			count = 0
			for num in nums:
				if num % divis == 0:
					count += 1

			if count > prev_count:
				prev_count = count
				res = divis
			elif count == prev_count:
				res = min(res, divis)

		return res
