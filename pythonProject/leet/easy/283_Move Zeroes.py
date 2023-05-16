from typing import *


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		p1, p2 = 0, 1
		N = len(nums)
		while p2 < N:
			if nums[p1] == 0 and nums[p2] != 0:
				nums[p2], nums[p1] = nums[p1], nums[p2]
			elif nums[p1] == 0 and nums[p2] == 0:
				while nums[p2] == 0 and p2 < N - 1:
					p2 += 1
				nums[p2], nums[p1] = nums[p1], nums[p2]
			p1 += 1
			p2 += 1
