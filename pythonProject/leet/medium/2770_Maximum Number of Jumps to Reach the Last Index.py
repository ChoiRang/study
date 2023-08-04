from typing import *


class Solution:
	def maximumJumps(self, nums: List[int], target: int) -> int:
		n = len(nums)
		dp = [0] + [1 if -target <= nums[i] - nums[0] <= target else -1 for i in range(1, n)]

		for i in range(1, n - 1):
			if dp[i] > 0:
				for j in range(i + 1, n):
					if -target <= nums[j] - nums[i] <= target:
						dp[j] = max(dp[j], dp[i] + 1)

		return dp[n - 1]
