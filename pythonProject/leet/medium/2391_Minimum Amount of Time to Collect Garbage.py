from typing import *
import collections


class Solution:
	def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
		fin = collections.defaultdict(int)
		total = 0

		for i, string in enumerate(garbage):
			for s in string:
				total += 1
				fin[s] = i

		for i in fin.items():
			total += sum(travel[:i[1]])

		return total
