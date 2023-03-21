from typing import *


class Solution2:
	def maximizeGreatness(self, nums: List[int]) -> int:
		nums.sort()
		res = 0
		for num in nums:
			if num > nums[res]:
				res += 1

		return res


# TLE
class Solution:
	def maximizeGreatness(self, nums: List[int]) -> int:
		nums.sort()
		num_sort = list(filter(lambda x: x > 0, nums))
		res = 0
		for num in nums:
			for idx2, num2 in enumerate(num_sort):
				if num2 > num:
					res += 1
					num_sort[idx2] = 0
					break

		return res
