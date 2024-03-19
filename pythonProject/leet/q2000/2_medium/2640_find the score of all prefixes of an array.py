from typing import *


class Solution:
	def findPrefixScore(self, nums: List[int]) -> List[int]:
		res = []
		max_val = 0
		score = 0
		for i in range(len(nums)):
			max_val = max(max_val, nums[i])
			score += nums[i] + max_val
			res.append(score)

		return res
