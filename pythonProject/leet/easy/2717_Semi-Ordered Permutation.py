from typing import *


class Solution:
	def semiOrderedPermutation(self, nums: List[int]) -> int:
		N = len(nums)
		i = nums.index(1)
		j = nums.index(N)
		if i > j:
			return N - 1 - j + i - 1
		else:
			return N - 1 - j + i

"""
semi-ordered => nums[0] == 1 and nums[len(nums-1] == len(nums)
"""
