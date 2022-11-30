from typing import *


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		count = 1
		for i in range(len(nums)):
			if nums[count - 1] < nums[i]:
				nums[count] = nums[i]
				count += 1

		return count