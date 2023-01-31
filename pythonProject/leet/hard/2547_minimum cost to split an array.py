import collections
from typing import *


class Solution:
	def minCost(self, nums: List[int], k: int) -> int:
		# @cache # python 3.9v
		def get_num(index):
			if index == len(nums):
				return 0
			cost = k
			best = 10 ** 10
			counter = collections.Counter()

			for i in range(index, len(nums)):
				counter[nums[i]] += 1

				if counter[nums[i]] == 2:
					cost += 2
				elif counter[nums[i]] > 2:
					cost += 1
				best = min(best, cost + get_num(i + 1))

			return best

		return get_num(0)


"""
---
Testcase
[1,2,1,2,1,3,3]
2
[1,2,1,2,1]
2
[1,2,1,2,1]
5
[2,3,3,3,1,5,5,0,5,3,4,2,1,2,5,1,2,0]
5
[5,6,4,3,2,5,4,1,5,2,0,5,4,3,1,5,4,3,4,4]
3
---
"""
