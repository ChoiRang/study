from functools import cache
from typing import *


class Solution:
	def maxScore(self, nums: List[int], x: int) -> int:
		n = len(nums)

		@cache
		def go(idx, parity):
			if idx == n:
				return 0

			if nums[idx] % 2 == parity:
				return max(go(idx + 1, parity) + nums[idx],
									 go(idx + 1, parity))
			else:
				return max(go(idx + 1, nums[idx] % 2) + nums[idx] - x,
									 go(idx + 1, parity))

		return nums[0] + go(1, nums[0] % 2)
