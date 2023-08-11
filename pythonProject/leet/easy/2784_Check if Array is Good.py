from typing import *


class Solution:
	def isGood(self, nums: List[int]) -> bool:
		n = len(nums)
		nums.sort()

		for i in range(n - 2):
			if nums[i] != i + 1:
				return False
		if nums[-1] != n - 1 or nums[-2] != n - 1:
			return False

		return True


# REF
class Solution2:
	def isGood(self, nums: List[int]) -> bool:
		max_num = max(nums)
		nums.remove(max_num)

		if len(nums) != max_num:
			return False
		else:
			for i in range(1, max_num + 1):
				if i not in nums:
					return False

		return True
