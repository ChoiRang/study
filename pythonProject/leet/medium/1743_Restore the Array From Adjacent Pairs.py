from typing import *
import collections


class Solution:
	def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
		n = len(adjacentPairs)
		pairs = collections.defaultdict(list)

		for x, y in adjacentPairs:
			pairs[x].append(y)
			pairs[y].append(x)

		for key in pairs.keys():
			if len(pairs[key]) == 1:
				res = [key]

		prev = None
		while pairs:
			curr = res[-1]
			for num in pairs[curr]:
				if num != prev:
					res.append(num)
			del pairs[curr]

			prev = curr

		return res
