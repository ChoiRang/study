from typing import *
import collections


class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		soldiers = collections.defaultdict(list)
		for i, row in enumerate(mat):
			soldiers[sum(row)].append(i)

		res = []

		for i in sorted(soldiers):
			res += soldiers[i]
		return res[:k]
