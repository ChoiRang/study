from typing import *


class Solution:
	def findTheArrayConcVal(self, nums: List[int]) -> int:
		N = len(nums)
		result = 0

		for i in range(N // 2):
			result += int(str(nums[i]) + str(nums[-1 - i]))

		if N % 2 == 1:
			result += nums[N // 2]
		return result
