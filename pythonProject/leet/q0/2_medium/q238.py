from typing import *


class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		left, right = [1] * n, [1] * n
		i, j = 1, n - 2
		while i < n:
			left[i] = left[i - 1] * nums[i - 1]
			right[j] = right[j + 1] * nums[j + 1]
			i += 1
			j -= 1

		return [left[i] * right[i] for i in range(n)]
