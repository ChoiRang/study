from typing import *


class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		i = 2 ** 31
		j = 2 ** 31
		for num in nums:
			if i > num:
				i = num
			if i < num < j:
				j = num
			if num > j:
				return True

		return False
