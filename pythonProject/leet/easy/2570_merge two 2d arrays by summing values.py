from typing import *
import collections


class Solution:
	def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
		nums = collections.Counter()
		result = []
		for x, y in nums1 + nums2:
			nums[x] += y
		for i in nums.keys():
			result.append([i, nums[i]])

		result.sort()

		return result
