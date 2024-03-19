from typing import *


class Solution:
	def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
		row, col = dict(), dict()
		row_sum, col_sum = 0, 0
		total = 0
		for ty, idx, val in reversed(queries):
			if ty == 0:
				if idx not in row:
					row_sum += 1
					row[idx] = val
					total += val * (n - col_sum)
			else:
				if idx not in col:
					col_sum += 1
					col[idx] = val
					total += val * (n - row_sum)

		return total
