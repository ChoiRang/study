from typing import *


class Solution:
	def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
		col = [len(str(x)) for x in grid[0]]

		for i in range(1, len(grid)):
			for idx, num in enumerate(grid[i]):
				col[idx] = max(col[idx], len(str(num)))

		return col
