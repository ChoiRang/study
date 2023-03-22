from typing import *


class Solution:
	def findScore(self, nums: List[int]) -> int:
		seen = set()
		sort_list = sorted(enumerate(nums), key=lambda x: (x[1], x[0]))
		count = 0

		for idx, num in sort_list:
			if idx in seen:
				continue
			count += num
			seen.add(idx)
			if idx > 0:
				seen.add(idx - 1)
			if idx < len(nums) - 1:
				seen.add(idx + 1)

		return count
