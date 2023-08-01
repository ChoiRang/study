from typing import *
import collections


# REF
class Solution:
	def continuousSubarrays(self, nums: List[int]) -> int:
		n = len(nums)
		res = 0
		left = 0
		dict1 = collections.defaultdict(int)

		for right in range(n):
			dict1[nums[right]] += 1
			while max(dict1.keys()) - min(dict1.keys()) > 2:
				dict1[nums[left]] -= 1
				if dict1[nums[left]] == 0:
					del dict1[nums[left]]
				left += 1

			res += right - left

		return res + n
