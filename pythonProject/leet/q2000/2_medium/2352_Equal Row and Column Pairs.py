from typing import *
import collections


class Solution:
	def equalPairs(self, grid: List[List[int]]) -> int:
		counter = collections.Counter()
		for row in grid:
			counter[tuple(row)] += 1

		total = 0
		N = len(grid)
		for i in range(N):
			row = []
			for j in range(N):
				row.append(grid[j][i])
			total += counter[tuple(row)]

		return total
