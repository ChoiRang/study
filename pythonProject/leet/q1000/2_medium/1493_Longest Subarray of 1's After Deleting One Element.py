from typing import *


class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		count = 0
		p1 = p2 = 0
		res = 0
		N = len(nums)
		while p1 < N and p2 < N:
			if nums[p2] == 0:
				count += 1

			if count == 2:
				res = max(res, p2 - p1 - 1)
				while count > 1 and p1 < p2:
					count -= int(nums[p1] == 0)
					p1 += 1
			p2 += 1

		res = max(res, p2 - p1 - 1)
		return res
