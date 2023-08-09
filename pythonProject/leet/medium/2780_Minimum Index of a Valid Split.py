from typing import *
import collections


class Solution:
	def minimumIndex(self, nums: List[int]) -> int:
		n = len(nums)
		count = collections.Counter(nums)
		elem, occur = 0, 0
		for key in count.keys():
			if count[key] > occur:
				elem = key
				occur = count[key]

		prefix = [0] * (n + 1)
		for i in range(n):
			prefix[i + 1] += prefix[i]
			if nums[i] == elem:
				prefix[i + 1] += 1
			if prefix[i + 1] * 2 > i + 1 and (occur - prefix[i + 1]) * 2 > n - i - 1:
				return i

		return -1


"""
# TLE
class Solution:
	def minimumIndex(self, nums: List[int]) -> int:
		n = len(nums)
		left = collections.Counter()
		right = collections.Counter(nums)

		for idx, num in enumerate(nums):
			left[num] += 1
			right[num] -= 1
			left_val, left_occur = left.most_common(1)[0]
			right_val, right_occur = right.most_common(1)[0]
			if left_val == right_val:
				if left_occur * 2 > (idx + 1) and right_occur * 2 > (n - idx - 1):
					return idx

		return -1
"""
