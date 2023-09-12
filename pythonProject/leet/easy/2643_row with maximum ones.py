from typing import *


class Solution:
	def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
		res1, res2 = 0, 0
		for idx, row in enumerate(mat):
			count = sum(row)
			if count > res2:
				res1 = idx
				res2 = count

		return [res1, res2]
