from typing import *


class Solution:
	def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
		res = []
		seen = {}
		for idx, size in enumerate(groupSizes):
			if size not in seen:
				seen[size] = []
			seen[size].append(idx)
			print(seen)
			if len(seen[size]) == size:
				res.append(seen[size])
				seen[size] = []

		return res
