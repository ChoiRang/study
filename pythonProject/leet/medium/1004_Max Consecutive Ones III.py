from typing import *


class Solution:
	def longestOnes(self, nums: List[int], k: int) -> int:
		p1 = p2 = 0
		res = 0
		zeros = 0
		N = len(nums)
		while p1 < N and p2 < N:
			if zeros < k or nums[p2] == 1:
				if nums[p2] == 0:
					zeros += 1
				p2 += 1
			else:
				if nums[p1] == 0:
					zeros -= 1
				p1 += 1
			res = max(res, p2 - p1)

		return res
