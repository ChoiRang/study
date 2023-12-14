from typing import *


class Solution:
	def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
		m, n = len(grid), len(grid[0])
		res = [[0] * n for _ in range(m)]
		col = [0] * n
		for i in range(m):
			for j in range(n):
				col[j] += grid[i][j]

		for i in range(m):
			row = sum(grid[i])
			for j in range(n):
				res[i][j] = 2 * row + 2 * col[j] - (m + n)

		return res
