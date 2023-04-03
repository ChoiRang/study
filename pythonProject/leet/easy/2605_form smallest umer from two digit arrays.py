from typing import *


class Solution:
	def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
		small = 100
		for num1 in nums1:
			for num2 in nums2:
				small = min(small, num1 * 10 + num2, num2 * 10 + num1)
				if num1 == num2:
					small = min(small, num1)
		return small
