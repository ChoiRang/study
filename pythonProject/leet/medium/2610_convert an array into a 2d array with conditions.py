import collections
from typing import *


class Solution:
	def findMatrix(self, nums: List[int]) -> List[List[int]]:
		res = [[nums[0]]]
		seen = collections.defaultdict(list)
		seen[nums[0]] = 0
		for i in range(1, len(nums)):
			num = nums[i]
			if num in seen:
				seen[num] += 1
			else:
				seen[num] = 0

			idx = seen[num]
			if len(res) <= idx:
				res.append([num])
			else:
				res[idx].append(num)

		return res
