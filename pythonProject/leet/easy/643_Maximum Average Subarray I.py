from typing import *


class Solution:
	def findMaxAverage(self, nums: List[int], k: int) -> float:
		cur = max_cur = sum(nums[:k])
		N = len(nums)
		for i in range(k, N):
			cur += nums[i] - nums[i - k]
			max_cur = max(max_cur, cur)

		return max_cur / k
