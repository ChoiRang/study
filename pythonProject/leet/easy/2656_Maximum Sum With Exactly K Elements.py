from typing import *


class Solution:
	def maximizeSum(self, nums: List[int], k: int) -> int:
		max_num = max(nums)
		res = 0
		for i in range(k):
			res += max_num
			max_num += 1

		return res
