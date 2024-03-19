from typing import *
import collections


class Solution:
	def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
		counter = collections.Counter(nums)

		for i in range(len(moveFrom)):
			if moveTo[i] == moveFrom[i]:
				continue
			counter[moveTo[i]] += counter[moveFrom[i]]
			del counter[moveFrom[i]]

		res = []
		for key in sorted(counter.keys()):
			res.append(key)

		return res
