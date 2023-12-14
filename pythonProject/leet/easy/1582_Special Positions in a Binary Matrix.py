from typing import *


class Solution:
	def numSpecial(self, mat: List[List[int]]) -> int:
		res = 0
		m, n = len(mat), len(mat[0])
		loc_x, loc_y = [0] * m, [0] * n
		for i in range(m):
			for j in range(n):
				if mat[i][j] == 1:
					loc_x[i] += 1
					loc_y[j] += 1

		for i in range(m):
			for j in range(n):
				if mat[i][j] == 1:
					if loc_x[i] == 1 and loc_y[j] == 1:
						res += 1
		return res
