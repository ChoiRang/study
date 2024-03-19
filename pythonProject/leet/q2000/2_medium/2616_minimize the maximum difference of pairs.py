from typing import *


class Solution:
	def minimizeMax(self, nums: List[int], p: int) -> int:
		N = len(nums)
		nums.sort()
		left, right = 0, max(nums)
		while left < right:
			mid = (left + right) // 2
			count, i = 0, 1
			while i < N:
				if nums[i] - nums[i - 1] <= mid:
					count += 1
					i += 2
				else:
					i += 1

			if count >= p:
				right = mid
			else:
				left = mid + 1

		return left
