from typing import *


class Solution:
	def maximumBeauty(self, nums: List[int], k: int) -> int:
		dp = [0] * (max(nums) + k + 2)
		for num in nums:
			dp[max(0, num - k)] += 1
			dp[num + k + 1] -= 1

		for i in range(1, max(nums) + k + 1):
			dp[i] += dp[i - 1]

		return max(dp)


"""
# TLE
class Solution:
	def maximumBeauty(self, nums: List[int], k: int) -> int:
		dp = [0] * (max(nums)+k+1)

		for num in nums:
			for idx in range(max(0, num-k), num+k+1):
				dp[idx] += 1

		return max(dp)
"""
